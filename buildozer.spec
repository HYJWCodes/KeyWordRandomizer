[app]

title = 장르 랜덤머신
package.name = randomizer
package.domain = org.marinegarden
source.dir = .
source.include_exts = py,csv,ttf
version = 1.0
requirements = python3,kivy==2.2.1,cython==0.29.36
orientation = portrait
fullscreen = 1

# Android build settings
android.api = 33
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21

# Permissions
android.permissions = INTERNET
android.allow_backup = 1

# Source inclusion
android.add_src = true

# Compatibility flags
android.use_androidx = 1
android.enable_androidx_workaround = 1

# Avoid Cython error: undeclared name 'long'
p4a.local_recipes = ./custom_recipes
