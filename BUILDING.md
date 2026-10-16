# Building

The Windows workflow packages the Ren'Py game as a ZIP containing an EXE. Open Actions > Windows build > Run workflow, then download the artifact from the completed run.

The Android workflow requires a valid signing keystore and repository secrets: ANDROID_KEYSTORE (base64-encoded keystore), ANDROID_KEYSTORE_PASSWORD, ANDROID_ALIAS_PASSWORD. Keep the keystore private and backed up. Open Actions > Android APK build > Run workflow. The APK is attached as an artifact if the build succeeds.

These workflows use the independently maintained MIT-licensed Ayowel/renpy-setup-action@v3. Review its security and licensing before relying on it for production. Android packaging also requires compatible Ren'Py/RAPT SDK and a valid .android.json. No successful build is claimed until Actions finishes.
