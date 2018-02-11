Lebab ES6 Transform for SublimeText 3
========================
A sublime package to easily transform your code to ES6

## Installation
#### Note
The plugin uses a bundled version of Lebab using [zeit/pkg](https://github.com/zeit/pkg) which produces three executables files for Windows, Linux and MacOs. Therefor this package **NO** longer needs the following:

1. No longer needs Nodejs. The bundled lebab versions are already packed with Nodejs v8.9.0
2. No longer needs Lebab package and any of it's dependencies. The bundles lebab already includes all necessary dependencies.

#### Install plugin
Please use [Package Control](https://sublime.wbond.net/installation) to install the plugin.

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.
2. When the plugin list appears, type `lebab`. Among the entries you should see `Lebab-ES6-Transform`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Options
**format_on_save:**

This will format your js file on each save. Default: true

**show_warnings:**

This will show any lebab warnings on your sublime panel. Default: true

**transforms:**

This plugin only enables the safest transforms from Lebab, but you can enable
all or any of them by changing the transforms option in your user settings.

NOTE: To see a full list of transforms visit [Lebab](https://github.com/lebab/lebab#safe-transforms)

Here are the default settings:

```json

{
  // runs lebab on the current js file upon saving
  "format_on_save": true,
  // shows the lebab warning message via sublime panel
  "show_warnings": true,
  // safe transforms https://github.com/lebab/lebab#safe-transforms
  "transforms": [
      "arrow",
      "arg-rest",
      "obj-method",
      "obj-shorthand",
      "class",
      "let",
      "includes",
      "template",
      "for-of",
      "exponent",
      "default-param",
      "commonjs"
  ]
}

```

## Contributing

If you find any bugs feel free to report them [here](https://github.com/uniibu/lebab-es6-transform/issues).

Pull requests are also encouraged.
