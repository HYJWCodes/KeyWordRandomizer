[app]

# App metadata
title = 로맨스 & BL 랜덤 키워드 머신
package.name = randomizer
package.domain = org.marinegarden
version = 1.0

# Source files
source.dir = .
source.include_exts = py,csv,ttf
source.exclude_dirs = tests,venv

# Main requirements
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Asset files
icon.filename = app_icon.png
presplash.filename = presplash.png
android.add_src = true

# Permissions (none)
android.permissions = 

# Android-specific config
android.minapi = 21
android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = armeabi-v7a, arm64-v8a

# Support for modern libraries
android.use_androidx = 1
android.enable_androidx_workaround = 1

# Enable backup
android.allow_backup = 1

# Use Android App Bundle
android.aab = True
