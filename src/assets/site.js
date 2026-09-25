// Erken erisim formu: form adresi tanimliysa oraya gonderir, degilse e-posta taslagi acar.
(function () {
  var form = document.getElementById("accessForm");
  if (!form) return;
  var status = document.getElementById("formStatus");
  var endpoint = form.getAttribute("data-endpoint");
  var email = form.getAttribute("data-email");

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
      say("Please add your name, a valid work email and your company.", "err");
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
      say("Sending…");
      fetch(endpoint, {
        method: "POST",
        headers: {"Content-Type": "application/json", "Accept": "application/json"},
        body: JSON.stringify(data)
      }).then(function (response) {
        if (!response.ok) throw new Error(String(response.status));
        form.reset();
        say("Thanks, we got it. We will get back to you soon.", "ok");
      }).catch(function () {
        say("That did not go through. Please email us at " + email + ".", "err");
      });
      return;
    }

    var body = "Name: " + data.name + "\nCompany: " + data.company + "\nEmail: " + data.email +
      "\nFCL containers per month: " + (data.volume || "-") + "\n\n" + (data.note || "");
    window.location.href = "mailto:" + email + "?subject=" + encodeURIComponent("WardOps early access: " + data.company) +
      "&body=" + encodeURIComponent(body);
    say("Your email app should open with the details filled in. If it does not, write to " + email + ".");
  });
})();
