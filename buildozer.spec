[app]

title = 장르 랜덤머신
package.name = randomizer
package.domain = org.marinegarden
source.dir = .
source.include_exts = py,csv,ttf
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Include files
presplash.filename = 
icon.filename = 

# Android permissions
android.permissions = INTERNET

# (Required for Korean font support)
android.allow_backup = 1
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# Kotlin (optional)
android.use_androidx = 1
android.enable_androidx_workaround = 1

# Buildozer spec snippet
android.api = 33
android.build_tools_version = 33.0.2
android.sdk = 33
android.ndk = 25b


# Copy fonts and csvs into .apk
android.add_src = true
