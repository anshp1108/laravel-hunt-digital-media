(function () {
  // Defensive wrapper to avoid errors when theme toggle buttons aren't present
  if (typeof window === 'undefined' || !window.Helpers) return;
  try {
    var orig = window.Helpers.showActiveTheme;
    if (typeof orig !== 'function') return;
    window.Helpers.showActiveTheme = function (theme) {
      var focus = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : false;
      try {
        var btnToActive = document.querySelector('[data-bs-theme-value="' + theme + '"]');
        if (!btnToActive) {
          var themeSwitcher = document.querySelector('#nav-theme');
          if (focus && themeSwitcher) {
            try { themeSwitcher.focus(); } catch (e) { /* ignore */ }
          }
          return;
        }
      } catch (e) {
        return;
      }
      return orig.apply(this, arguments);
    };
  } catch (e) {
    // ignore
  }
})();
