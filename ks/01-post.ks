%post

#Edit firefox to point to mesa
for i in /usr/lib64/firefox/browser/firefox-redhat-default-prefs.js /usr/lib64/firefox/browser/defaults/preferences/firefox-redhat-default-prefs.js
do
cat > $i << EOF

pref("app.update.auto",                     false);
pref("app.update.enabled",                  false);
pref("app.update.autoInstallEnabled",       false);
pref("general.smoothScroll",                true);
pref("intl.locale.matchOS",                 true);
pref("toolkit.storage.synchronous",         0);
pref("toolkit.networkmanager.disable",      false);
pref("offline.autoDetect",                  true);
pref("browser.backspace_action",            2);
pref("browser.display.use_system_colors",   true);
pref("browser.download.folderList",         1);
pref("browser.link.open_external",          3);
pref("browser.shell.checkDefaultBrowser",   false);
pref("network.manage-offline-status",       true);
pref("extensions.shownSelectionUI",         true);
pref("gfx.color_management.enablev4",       true);
pref("ui.SpellCheckerUnderlineStyle",       1);
pref("browser.startup.homepage_override.mstone", "ignore");
pref("browser.startup.homepage",            "data:text/plain,browser.startup.homepage=http://mesa.sourceforge.net/");
pref("browser.newtabpage.pinned",           '[{"url":"http://mesa.sourceforge.net/","title":"MESA Project"}]');
pref("geo.wifi.uri", "https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%");
pref("media.gmp-gmpopenh264.provider.enabled",false);
pref("media.gmp-gmpopenh264.autoupdate",false);
pref("media.gmp-gmpopenh264.enabled",false);
pref("media.gmp-gmpopenh264.enabled",false);
pref("plugins.notifyMissingFlash", false);
/* See https://bugzilla.redhat.com/show_bug.cgi?id=1226489 */
pref("browser.display.use_system_colors", false);

EOF
done

%end