// Erken erisim formu: form adresi tanimliysa oraya gonderir, degilse e-posta taslagi acar.
(function () {
  var form = document.getElementById("accessForm");
  if (!form) return;
  var status = document.getElementById("formStatus");
  var endpoint = form.getAttribute("data-endpoint");
  var email = form.getAttribute("data-email");
  // Türkçe sayfada (lang="tr") mesajlar Türkçe.
  var tr = document.documentElement.lang === "tr";
  var T = tr ? {
    missing: "Lütfen adınızı, geçerli bir iş e-postasını ve firma adını yazın.", sending: "Gönderiliyor…",
    ok: "Teşekkürler, bilgileriniz bize ulaştı. En kısa sürede dönüş yapacağız.",
    fail: "Gönderilemedi. Lütfen şu adrese yazın: ", mail: "E-posta uygulamanız bilgiler dolu olarak açılmalı. Açılmazsa şu adrese yazın: ",
    subject: "WardOps erken erişim: ", fields: ["Ad", "Firma", "E-posta", "Aylık FCL konteyner"]
  } : {
    missing: "Please add your name, a valid work email and your company.", sending: "Sending…",
    ok: "Thanks, we got it. We will get back to you soon.",
    fail: "That did not go through. Please email us at ", mail: "Your email app should open with the details filled in. If it does not, write to ",
    subject: "WardOps early access: ", fields: ["Name", "Company", "Email", "FCL containers per month"]
  };

  function say(text, kind) {
    status.textContent = text;
    status.className = "form-status" + (kind ? " " + kind : "");
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (form.website && form.website.value) return;           // bot tuzagi doluysa sessizce dur
    var missing = [];
    ["name", "email", "company"].forEach(function (key) {
      var field = form.elements[key];
      var bad = !field.value.trim() || (key === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(field.value.trim()));
      field.setAttribute("aria-invalid", bad ? "true" : "false");
      if (bad) missing.push(field);
    });
    if (missing.length) {
      say(T.missing, "err");
      missing[0].focus();
      return;
    }
    var data = {
      name: form.elements.name.value.trim(),
      email: form.elements.email.value.trim(),
      company: form.elements.company.value.trim(),
      volume: form.elements.volume.value,
      note: form.elements.note.value.trim()
    };

    if (endpoint) {
      say(T.sending);
      fetch(endpoint, {
        method: "POST",
        headers: {"Content-Type": "application/json", "Accept": "application/json"},
        body: JSON.stringify(data)
      }).then(function (response) {
        if (!response.ok) throw new Error(String(response.status));
        form.reset();
        say(T.ok, "ok");
      }).catch(function () {
        say(T.fail + email + ".", "err");
      });
      return;
    }

    var body = T.fields[0] + ": " + data.name + "\n" + T.fields[1] + ": " + data.company + "\n" + T.fields[2] + ": " + data.email +
      "\n" + T.fields[3] + ": " + (data.volume || "-") + "\n\n" + (data.note || "");
    window.location.href = "mailto:" + email + "?subject=" + encodeURIComponent(T.subject + data.company) +
      "&body=" + encodeURIComponent(body);
    say(T.mail + email + ".");
  });
})();

// Ana sayfa yolculuk sahnesi: bolum ekrana yapisir, kaydirma ilerledikce sahne oynar.
// JavaScript yoksa veya azaltilmis hareket isteniyorsa sahne sabit kalir, uc adim metni okunur.
(function () {
  var section = document.getElementById("journey");
  if (!section) return;
  var part = function (name) { return section.querySelector('[data-j="' + name + '"]'); };
  var el = {};
  ["world", "ship", "box", "ring", "tag", "doc", "eta", "eta1", "eta2", "mail", "cust", "custok", "custwait",
   "trolley", "cable", "truck", "waves", "clouds", "r1", "r2", "r3"].forEach(function (name) { el[name] = part(name); });
  var steps = section.querySelectorAll(".journey-steps li");
  var svg = section.querySelector(".journey-svg");
  var track = section.querySelector(".journey-track");

  var SHIP_FROM = 270, SHIP_TO = 1750, SLOT_X = 226, SLOT_Y = -52, BOX_TRUCK_X = 2288, BOX_TRUCK_Y = 256;
  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
  function seg(p, a, b) { return clamp((p - a) / (b - a), 0, 1); }
  function ease(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function move(node, x, y, s) {
    node.setAttribute("transform", "translate(" + x.toFixed(1) + " " + y.toFixed(1) + ")" + (s ? " scale(" + s.toFixed(3) + ")" : ""));
  }
  function fade(node, value) { node.setAttribute("opacity", value.toFixed(3)); }

  function render(p) {
    // Dar ekranda sahnenin tamamı yerine hareketin olduğu bölge gösterilir (yazılar okunur kalsın).
    var narrow = window.innerWidth < 640;
    var viewW = narrow ? 540 : 1200;
    var viewX = narrow ? lerp(10, 650, ease(seg(p, 0.26, 0.38))) : 0;
    svg.setAttribute("viewBox", viewX.toFixed(1) + " 0 " + viewW + " 460");
    var custX = viewX + viewW - 256;
    move(el.cust, custX, 30);
    move(el.r1, viewX + 32, 30);
    move(el.r2, viewX + 32, 74);
    move(el.r3, viewX + 32, 118);

    // 1) belge uçar, konteynere yerleşir
    var f = ease(seg(p, 0.04, 0.24));
    var docX = (1 - f) * (1 - f) * 150 + 2 * (1 - f) * f * 360 + f * f * 520;
    var docY = (1 - f) * (1 - f) * 130 + 2 * (1 - f) * f * 10 + f * f * 261;
    move(el.doc, docX, docY, lerp(1, 0.16, f));
    fade(el.doc, 1 - seg(p, 0.2, 0.25));
    fade(el.ring, seg(p, 0.2, 0.26));
    fade(el.tag, seg(p, 0.22, 0.28));

    // 2) gemi kalkar; kamera gemiyi izler
    var voyage = ease(seg(p, 0.3, 0.72));
    var shipX = lerp(SHIP_FROM, SHIP_TO, voyage);
    var bob = voyage > 0 && voyage < 1 ? Math.sin(p * 90) * 1.6 : 0;
    var cam = clamp(shipX - 510, 0, 1240);
    move(el.world, -cam, 0);
    move(el.ship, shipX, 300 + bob);
    move(el.waves, -((cam * 0.6 + p * 240) % 120), 0);
    move(el.clouds, -cam * 0.12, 0);

    fade(el.eta, seg(p, 0.38, 0.42) * (1 - seg(p, 0.68, 0.72)));
    fade(el.eta1, 1 - seg(p, 0.48, 0.5));
    fade(el.eta2, seg(p, 0.48, 0.5));
    var m = ease(seg(p, 0.53, 0.61));
    var fromX = shipX + 196 - cam, fromY = 170;
    move(el.mail, lerp(fromX, custX + 28, m), lerp(fromY, 57, m) - Math.sin(m * Math.PI) * 60);
    fade(el.mail, seg(p, 0.52, 0.54) * (1 - seg(p, 0.6, 0.62)));
    fade(el.cust, seg(p, 0.46, 0.5));
    fade(el.custok, seg(p, 0.6, 0.63));
    fade(el.custwait, 1 - seg(p, 0.6, 0.62));

    // 3) vinç konteyneri kamyona indirir, kamyon yola çıkar
    var dockX = SHIP_TO + SLOT_X;
    var drive = ease(seg(p, 0.93, 1)) * 28;
    var boxX = shipX + SLOT_X, boxY = 300 + SLOT_Y + bob;
    if (p >= 0.76) { boxX = dockX; boxY = lerp(248, 160, seg(p, 0.76, 0.81)); }
    if (p >= 0.81) { boxX = lerp(dockX, BOX_TRUCK_X, ease(seg(p, 0.81, 0.87))); boxY = 160; }
    if (p >= 0.87) { boxX = BOX_TRUCK_X; boxY = lerp(160, BOX_TRUCK_Y, seg(p, 0.87, 0.91)); }
    if (p >= 0.91) { boxX = BOX_TRUCK_X + drive; boxY = BOX_TRUCK_Y; }
    move(el.box, boxX, boxY);
    move(el.truck, drive, 0);
    var trolleyX = p < 0.76 ? dockX + 24 : (p < 0.91 ? boxX + 24 : BOX_TRUCK_X + 24);
    move(el.trolley, trolleyX, 0);
    el.cable.setAttribute("x1", trolleyX.toFixed(1));
    el.cable.setAttribute("x2", trolleyX.toFixed(1));
    el.cable.setAttribute("y2", (p < 0.76 ? 226 : (p < 0.91 ? boxY : lerp(boxY, 150, seg(p, 0.91, 0.94)))).toFixed(1));
    fade(el.r1, seg(p, 0.78, 0.8));
    fade(el.r2, seg(p, 0.82, 0.84));
    fade(el.r3, seg(p, 0.9, 0.92));

    var active = p < 0.28 ? 0 : (p < 0.74 ? 1 : 2);
    for (var i = 0; i < steps.length; i++) steps[i].classList.toggle("on", i === active);
  }

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { render(1); return; }
  section.classList.add("is-scroll");
  var header = document.querySelector(".site-header");
  var pending = false;
  function update() {
    pending = false;
    var top = header ? header.offsetHeight : 0;
    var box = track.getBoundingClientRect();
    var range = box.height - (window.innerHeight - top);
    render(range > 0 ? clamp((top - box.top) / range, 0, 1) : 0);
  }
  function schedule() { if (!pending) { pending = true; window.requestAnimationFrame(update); } }
  window.addEventListener("scroll", schedule, {passive: true});
  window.addEventListener("resize", schedule);
  update();
})();

// Tanitim videosu: kapak uzerindeki oynat dugmesi (JS yoksa tarayicinin kendi oynaticisi calisir).
(function () {
  var video = document.getElementById("launch-video");
  if (!video) return;
  var button = video.parentNode.querySelector(".video-play");
  if (!button) return;
  // Kapakta yalnizca bizim dugmemiz gorunsun; oynatma baslayinca tarayicinin kontrolleri geri gelir.
  video.controls = false;
  button.hidden = false;
  function hide() { button.hidden = true; video.controls = true; }
  button.addEventListener("click", function () {
    hide();
    var played = video.play();
    if (played && played.catch) played.catch(function () { button.hidden = false; video.controls = false; });
  });
  video.addEventListener("play", hide);
})();

// Fiyat sayfasi: aylik / yillik odeme secici (JS yoksa aylik fiyatlar gorunur).
(function () {
  var buttons = document.querySelectorAll("[data-billing]");
  if (!buttons.length) return;
  function show(period) {
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute("aria-pressed", String(buttons[i].getAttribute("data-billing") === period));
    }
    var values = document.querySelectorAll("[data-monthly][data-yearly]");
    for (var k = 0; k < values.length; k++) {
      values[k].textContent = values[k].getAttribute(period === "yearly" ? "data-yearly" : "data-monthly");
    }
  }
  for (var b = 0; b < buttons.length; b++) {
    buttons[b].addEventListener("click", function () { show(this.getAttribute("data-billing")); });
  }
})();
