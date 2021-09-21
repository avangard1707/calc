[app]


title = Mobile App 001


package.name = mobileapp001


package.domain = org.wiseplat


source.dir = .


version = 0.1


requirements = python3,kivy==2.0.0


orientation = all


osx.python_version = 3


osx.kivy_version = 2.0.0


fullscreen = 0



android.arch = armeabi-v7a

android.allow_backup = True

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ub.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0


ios.codesign.allowed = false


[buildozer]

warn_on_root = 1


