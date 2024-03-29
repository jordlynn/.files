LaTeX Plugin for Sublime Text 2 and 3
=====================================

by Ian Bacher and Marciano Siniscalchi

Marciano's blog:
[http://tekonomist.wordpress.com]


Additional contributors (*thank you thank you thank you*): first of all, Wallace Wu and Juerg Rast, who contributed code for multifile support in ref and cite completions, "new-style" ref/cite completion, and project file support. Also, skuroda (Preferences menu), Sam Finn (initial multifile support for the build command); Daniel Fleischhacker (Linux build fixes), Mads Mobaek (universal newline support), Stefan Ollinger (initial Linux support), RoyalTS (aka Tobias Schidt?) (help with bibtex regexes and citation code, various fixes), Juan Falgueras (latexmk option to handle non-ASCII paths), Jeremy Jay (basic biblatex support), Ray Fang (texttt snippet), Ulrich Gabor (tex engine selection and cleaning aux files), Wes Campaigne and 'jlegewie' (ref/cite completion 2.0!). **Huge** thanks to Daniel Shannon (aka phyllisstein) who first ported LaTeXTools to ST3. Also thanks for Charley Peng, who has been assisting users and generating great pull requests; I'll merge them as soon as possible. Also William Ledoux (various Windows fixes, env support), Sean Zhu (find Skim.app in non-standard locations), Maximilian Berger (new center/table snippet), Lucas Nanni (recursively delete temp files), Sergey Slipchenko (`$` auto-pairing with Vintage) Ian Bacher (use `kpsewhich` to find bib files in the `TEXMF` tree; reworked fill-all command; jump to tex files improvements; delete temp files improvements; builder options; improved LaTeX-cwl support), btstream (original fill-all command; LaTeX-cwl support), Richard Stein (auto-hide build panel, jump to included tex files, LaTeX-cwl support config, TEX spellcheck support, functions to analyze LaTeX documents, cache functionality), Dan Schrage (nobibliography command), PoByBolek (more biblatex command), Rafael Lerm (support for multiple lines in `\bibliography` commands).

*If you have contributed and I haven't acknowledged you, email me!*

*Latest revision:* v3.7.9 (2016-04-26).

*Headline features*:

  * New viewers for Preview.app and Okular
  * New bibliography parser available (see the settings file)
  * Support for most citation commands, especially using BibLaTeX

*Reminder*: See the [Settings section](#settings) for details on the Settings system, which was updated in v3.6.1 (2016-01-01).

**Note**: If you've been following along with the v3.7.x release, v3.7.7 is a major change. I've restored the previous bibliography parsing from v3.6 and earlier as default. If you want to use the new parsing, you need to change the `bibliography` setting to `"new_bibliography"`. Thanks to everyone who has filed bug reports. At present, all the reported bugs should be resolved, but I'm not certain that some don't remain (BibTeX is a wild world) and the older parsing seems to be substantially faster for those with extremely large bibliographies.



Introduction
------------
This plugin provides several features that simplify working with LaTeX files:

* The ST build command takes care of compiling your LaTeX source to PDF using `texify` (Windows/MikTeX) or `latexmk` (OSX/MacTeX, Windows/TeXlive, Linux/TeXlive). Then, it parses the log file and lists errors and warning. Finally, it launches (or refreshes) the PDF viewer (SumatraPDF on Windows, Skim on OSX, and Evince on Linux by default) and jumps to the current cursor position.
* Forward and inverse search with the named PDF previewers is fully supported
* Easy insertion of references and citations (from BibTeX files)
* Plugs into the "Goto anything" facility to make jumping to any section or label in your LaTeX file(s)
* Smart command completion for a variety of text and math commands is provided
* Additional snippets and commands are also provided
* The build command is fully customizable, as is the PDF previewer.

Requirements and Setup
----------------------

First, you need to be running Sublime Text 2 or 3 (ST2 and ST3 henceforth, or simply ST to refer to either ST2 or ST3). For ST3, this has been tested against the latest beta builds.

Second, get the LaTeXTools plugin. These days, the easiest way to do so is via Package Control: see [here](https://sublime.wbond.net) for details on how to set it up (it's very easy). Once you have Package Control up and running, invoke it (via the Command Palette from the Tools menu, or from Preferences), select the Install Package command, and look for LaTeXTools.

If you prefer a more hands-on approach, you can always clone the git repository, or else just grab this plugin's .zip file from GitHub and extract it to your Packages directory (you can open it easily from ST, by clicking on Preferences|Browse Packages). Then, (re)launch ST. Please note that if you do a manual installation, the Package **must** be named "LaTeXTools".

I encourage you to install Package Control anyway, because it's awesome, and it makes it easy to keep your installed packages up-to-date (see the aforelinked page for details). 

Third, follow the OS-specific instructions below.

<br>

On **OSX**, you need to be running the MacTeX distribution (which is pretty much the only one available on the Mac anyway). Just download and install it in the usual way. I have tested MacTeX versions 2010--2014, both 32 and 64 bits; these work fine. MacTeX 2015 also works. On the other hand, MacTeX 2008 does *not* seem to work out of the box (compilation fails), so please upgrade.

It is recommended that you install the Skim PDF viewer, as this provides support for forward and inverse search. By default, LaTeXTools assumes that you're using Skim. If you're not using Skim, see the section on viewers below.

**El Capitan note**: sadly, with each OS X release, Apple deviates more and more from established Unix conventions. The latest "innovation" is that, beginning with El Capitan, apps can no longer write to `/usr`. MacTeX 2015 remedies this by creating a link to TeX binaries in `/Library/TeX`. The default LaTeXTools settings file now adds `/Library/TeX/texbin` to the `texpath`. In practice, this means the following.

* If you are running MacTeX 2015 and have *not* customized the `texpath` option in your user settings file, you do not need to take further action.

* If you are running MacTex 2015 and have customized `texpath`, open your user settings file (remember, you can do so from the `Preferences | Package Settings | LaTeXTools` submenu) and add `/Library/TeX/texbin` as the first entry in `texpath`.

* If you are running earlier MacTeX versions, unfortunately you do *not* have the `/Library/TeX/texbin` link at all, so adding that path to `texpath` would not help. You have two options: create the link yourself, or edit the `texpath` option to point to the appropriate directory. Check Section 8 of [this document](https://tug.org/mactex/UpdatingForElCapitan.pdf) for details.

Sorry for the complications. It's not my fault.

If you don't want to install the entire MacTeX distro, which is pretty big, BasicTeX will also work (of course, as long as the latex packages you need are included). **However**, you need to explicitly add the `latexmk` utility, which is not included by default: from the Terminal, type `sudo tlmgr install latexmk` (you will need to provide your password, assuming you are Administrator on your machine).

To configure inverse search, open the Preferences dialog of the Skim app, select the Sync tab, then:

* uncheck the "Check for file changes" option
* choose the Sublime Text 2 or Sublme Text 3 preset (yes, Skim now supports both ST2 and ST3 by default!)

In case you are using an old version of Skim, you can always choose the Custom preset and enter `/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl` (for ST3) in the Command field, and `"%file":%line` in the Arguments field. (This is correct as of 7/18/2013; you may want to double-check that ST3 is indeed in `/Applications/Sublime Text`; just go to the Applications folder in the Finder. Adapt as needed for ST2).

Finally, edit the file `LaTeXTools.sublime-settings` in the `User` directory to make sure that the configuration reflects your preferred TeX distribution. Open the file and scroll down to the  section titled "Platform settings." Look at the block for your OS, namely `"osx"`. Within that block, verify that the `"texpath"` setting is correct. Note that `"texpath"` **must** include `$PATH` somewhere.

<br>

On **Windows**, both MikTeX and TeXlive are supported. It is recommded that you use the Sumatra PDF viewer, as using another viewer will require more configuration, but see the section on viewers below. If you do use Sumatra, you must be running a current (>=1.4) version. Install these as usual. If you are using Sumatra, add the SumatraPDF directory to your PATH or configure the `sumatra` setting in the `windows` platform setting of your `LaTeXTools.sublime-settings` in your **User** directory.

You now need to set up inverse search in Sumatra PDF. However, the GUI for doing this is hidden in Sumatra until you open a PDF file that has actual synchronization information (that is, an associated `.synctex.gz` file): see [here](http://forums.fofou.org/sumatrapdf/topic?id=2026321). If you have one such file, then open it, go to **Settings|Options**, and enter `"C:\Program Files\Sublime Text 2\sublime_text.exe" "%f:%l"` for ST2, and `"C:\Program Files\Sublime Text 3\sublime_text.exe" "%f:%l"` for ST3, as the inverse-search command line (in the text-entry field at the bottom of the options dialog). If you don't already have a file with sync information, you can easily create one: compile any LaTex file you already have (or create a new one) with `pdflatex -synctex=1 <file.tex>`, and then open the resulting PDF file in SumatraPDF. 

As an alternative, you can open a command-line console (run `cmd.exe`), and issue the following command:

	sumatrapdf.exe -inverse-search "\"C:\Program Files\Sublime Text 2\sublime_text.exe\" \"%f:%l\""

(this assumes that sumatraPDF is in your path; replace 2 with 3 for ST3 of course). I'm sorry this is not straightforward---it's not my fault :-)

Recent versions of MikTeX add themselves to your path automatically, but in case the build system does not work, that's the first thing to check. TeXlive can also add itself to your path.

Finally, edit the file `LaTeXTools.sublime-settings` in the `User` directory to make sure that the configuration reflects your preferred TeX distribution. Open the file and scroll down to the  section titled "Platform settings." Look at the block for your OS, namely `windows`. Within that block, verify that the `texpath` setting is correct; for MiKTeX, you can leave this empty, i.e., `""`. If you do specify a path, note that it **must** include the system path variable, i.e., `$PATH` (this syntax seems to be OK). Also verify that the `distro` setting is correct: the possible values are `"miktex"` and `"texlive"`.

TeXlive has one main advantage over MikTeX: it supports file names and paths with spaces.

<br>

**Linux** support is coming along nicely. However, as a general rule, you will need to do some customization before things work. This is due to differences across distributions (a.k.a. "fragmentation"). Do not expect things to work out of the box.

You need to install TeXlive; if you are on Ubuntu, note that `apt-get install texlive` will get you a working but incomplete setup. In particular, it will *not* bring in `latexmk`, which is essential to LaTeXTools. You need to install it via `apt-get install latexmk`. If on the other hand you choose to install the TeXlive distro from TUG, `latexmk` comes with it, so you don't need to do anything else. Also, to get inverse search working on ST3, make sure you set the `sublime` option in `LaTeXTools.sublime-settings` correctly; the Ubuntu package from the ST web page uses `subl`, but check from the command line first.

You also need to edit the file `LaTeXTools.sublime-settings` in the `User` directory to make sure that the configuration reflects your preferred TeX distribution.  Open that file and scroll down to the  section titled "Platform settings." Look at the block for your OS, namely `"linux"`. Within that block, verify that the `"texpath"` setting is correct. Notice that this **must** include `$PATH` somewhere, or things will not work.

You may also have to set the `command` option in `"builder_settings"`, which tells the builder how to invoke `latexmk`. By default (i.e., if `command` is empty or not given) it is `["latexmk", "-cd", "-e", "-f", "-pdf", "-interaction=nonstopmode", "-synctex=1"]`.

If you customize the command to include a custom PDF command, users have reported the following possible issues and fixes (thanks!), so if you get a "Cannot compile!" error, try the following:

* some distros do *not* want a space before and after the `=` in `$pdflatex = %E`. But some *do* want the space there (sigh!)
* sometimes `latexmk` is not on the `PATH`, or the path is not correctly picked up by ST. In this case, instead of `"latexmk"`, use `"/usr/bin/latexmk"` or wherever `latexmk` is in your system. 
* some distros require quoting the `$pdflatex` assignment, as in `"$pdflatex = \"'%E -interaction=nonstopmode -synctex=1 %S %O'\""`

There are several variants to deal with; each distro is a little bit different, so there are basically no universal defaults. There's not much I can do about it. Good luck! 

Only support for the Evince PDF viewer is built-in, but see the section on viewers below for details on how to setup other viewers. Evince is installed by default on Ubuntu or, more generally, any distro that provides the Gnome desktop, and you don't need to configure anything. Backward and forward search Work For Me (TM). Hopefully they will work for you, too, but let me know if this is not the case.


Keybindings
-----------

Keybindings have been chosen to make them easier to remember, and also to minimize clashes with existing (and standard) ST bindings. I am taking advantage of the fact that ST supports key combinations, i.e. sequences of two (or more) keys. The basic principle is simple:

- **Most LaTeXTools facilities are triggered using `Ctrl+l` (Windows, Linux) or `Cmd+l` (OS X), followed by some other key or key combination**

- Compilation uses the standard ST "build" keybinding, i.e. `Ctrl-b` on Windows and Linux and `Cmd-b` on OS X. So does the "goto anything" facility (though this may change).

For example: to jump to the point in the PDF file corresponding to the current cursor position, use `Ctrl-l, j`: that is, hit `Ctrl-l`, then release both the `Ctrl` and the `l` keys, and quickly type the `j` key (OS X users: replace `Ctrl` with `Cmd`). To wrap the selected text in an `\emph{}` command, use `Ctrl-l, Ctrl-e`: that is, hit `Ctrl-l`, release both keys, then hit `Ctrl-e` (again, OS X users hit `Cmd-l` and then `Cmd-e`). 

`Ctrl-l` (`Cmd-l` on OS X) is the standard ST keybinding for "expand selection to line"; this is **remapped** to `Ctrl-l,Ctrl-l` (`Cmd-l,Cmd-l` on OS X). This is the *only* standard ST keybinding that is affected by the plugin---an advantage of new-style keybindings.

Most plugin facilities are invoked using sequences of 2 keys or key combinations, as in the examples just given. A few use sequences of 3 keys or key combinations.

Henceforth, I will write `C-` to mean `Ctrl-` for Linux or Windows, and `Cmd-` for OS X. You know your platform, so you know what you should use. In a few places, to avoid ambiguities, I will spell out which key I mean.


Compiling LaTeX files
---------------------

**Keybinding:** `C-b` (standard ST keybinding)

LaTeXTools offers a fully customizable build process. This section describes the default process, also called "traditional" because it is the same (with minor tweaks) as the one used in previous releases. However, see below for how to customize the build process.

The default ST Build command takes care of the following:

* It saves the current file
* It invokes the tex build command (`texify` for MikTeX; `latexmk` for TeXlive and MacTeX).
* It parses the tex log file and lists all errors, warnings and, if enabled, bad boxes in an output panel at the bottom of the ST window: click on any error/warning/bad boxes to jump to the corresponding line in the text, or use the ST-standard Next Error/Previous Error commands.
* It invokes the PDF viewer for your platform and performs a forward search: that is, it displays the PDF page where the text corresponding to the current cursor position is located.

**Project files** are fully supported! Some of the options related to building `tex` files are described here. However, you should consult the [subsection on project-specific settings](#project-specific-settings) for further details. 

**Multi-file documents** are supported as follows. If the first line in the current file consists of the text `%!TEX root = <master file name>`, then tex & friends are invoked on the specified master file, instead of the current one. Note: the only file that gets saved automatically is the current one. Also, the master file name **must** have a valid tex extension (i.e., one configured in the `tex_file_exts` settings), or it won't be recognized. 

As an alternative, to using the `%!TEX root = <master file name>` syntax, if you use a Sublime project, you can set the `TEXroot` option (under `settings`):
	
```json
{
	... <folder-related settings> ...

	"settings": {
		"TEXroot": "yourfilename.tex"
	}
}
```

Note that if you specify a relative path as the `TEXroot` in the project file, the path is determined *relative to the location of the project file itself*. It may be less ambiguous to specify an absolute path to the `TEXroot` if possible.

**TeX engine selection** is supported. If the first line of the current file consists of the text `%!TEX program = <program>`, where `program` is `pdflatex`, `lualatex` or `xelatex`, the corresponding engine is selected. If no such directive is specified, `pdflatex` is the default. Multi-file documents are supported: the directive must be in the *root* (i.e. master) file. Also, for compatibility with TeXshop, you can use `TS-program` instead of `program`. **Note**: for this to work, you must **not** customize the `command` option in `LaTeXTools.sublime-settings`. If you do, you will not get this functionality. Finally, if you use project files, the `program` builder setting can also be customized there, under `settings`.

**TeX options**: you can pass TeX options to your engine in two ways (thanks Ian Bacher!). One is to use a `%!TEX options = ...` line at the top of your file. The other is to use the `options` builder setting in your settings file. This can be useful, for instance, if you need to allow shell escape. Finally, if you use project files, the `options` builder setting can also be customized there (again, under `settings`).

**Customizing or replacing the compilation command** (`latexmk` or `texify`) is also possible by setting the `command` option under Builder Settings. If you do, the TeX engine selection facility may no longer work because it relies on a specific compilation command. However, if you want to customize or replace `latexmk`/`texify`, you probably know how to select the right TeX engine, so this shouldn't be a concern. Also note that if you are using `latexmk` and you set the `$pdflatex` variable, the TeX options facility will not function, as `latexmk` does not support this. See the Settings option below for details. *Note*: if you change the compilation command, you are responsible for making it work on your setup. Only customize the compilation command if you know what you're doing. 


### Toggling window focus following a build ###

**Keybinding:** `C-l,t,f` (yes, this means `C-l`, then `t`, then `f`)

By default, after compilation, the focus stays on the ST window. This is convenient if you like to work with the editor and PDF viewer window open side by side, and just glance at the PDF output to make sure that all is OK. If however the editor and viewer windows overlap (e.g. if you have a small screen), you may prefer the viewer window to get the focus (i.e. become the foremost window) after compiling. To this end, you can use the `toggle_focus` command to change this behavior. The first time you invoke this command, the focus will shift to the viewer window after compiling the current file; if you invoke the command again, the post-compilation focus reverts to the editor window. Every time you invoke `toggle_focus`, a message will appear in the status bar.

You can change the default focus behavior via the `keep_focus` option: see the "Settings" section below.

### Toggling PDF syncing (forward search) following a build ###

**Keybinding:** `C-l,t,s`

By default, after compilation, LaTeXTools performs a 'forward search' so that the PDF viewer shows the point in the PDF file corresponding to the current cursor position in ST (by the way, you can trigger a forward search at any other time, not just when you are compiling: see below). If for whatever reason you don't like this behavior, you can turn it off using the `toggle_fwdsync` command. As for `toggle_focus`, a message will appear in the status bar to reflect this.

You can also change the default sync behavior via the `forward_sync` option: see the "Settings" section below.

### Checking the status of toggles and defaults ###

**Keybinding:** `C-l,t,?`

This causes the status message to list the default settings of the focus and sync options, and their current toggle values. It also display the status of the ref/cite auto trigger toggles (see below).

### Removing temporary files from build ###

**Keybinding:** `C-l,backspace`

This deletes all temporary files from a previous build (the PDF file is kept). Subfolders are traversed recursively.

Two settings allow you to fine-tune the behavior of this command. `temp_files_exts` allows you to specify which file extensions should be considered temporary, and hence deleted. `temp_files_ignored_folders` allows you to specify folders that should not be traversed. A good example are `.git` folders, for people who use git for version control.


### Automatically hide build panel after build finished ###

To automatically hide the build panel set the option `hide_build_panel` in the settings file. Possible values are:

- __always__: always hide the panel even if the build failed
- __no_errors__: only hide the panel if the build was successful althrough warnings appear
- __no_warnings__: only hide the build panel if neither errors nor warnings occur
- __no_badboxes__: only hide the build panel if there are no errors, warnings, or bad boxes
- __never__: never hide the build panel

Forward and Inverse Search
---------------------------

**Keybinding:** `C-l,j` (for forward search; inverse search depends on the previewer)

When working in an ST view on a TeX document, `C-l,j` will display the PDF page where the text corresponding to the current cursor position is located; this is called a "forward search". The focus is controlled by the `C-l,t,f` toggle setting and the `keep_focus` option.

If you are viewing a PDF file, then hitting `CMD+Shift+Click` in Skim (OSX), double-clicking in Sumatra (Windows), or hitting `Ctrl+click` in Evince (Linux) will bring you to the location in the source tex file corresponding to the PDF text you clicked on. This is called "inverse search".

To open a PDF file without performing a forward search, use `C-l,v`.

For support of forward and inverse search in other viewers, see the viewer section below.

References and Citations
------------------------

**Keybinding:** *autotriggered* by default (see below). Otherwise, `C-l,x` for 'cross-reference,' or `C-l,C-f` (via the Fill Helper facility: see below). These are fully equivalent ways of invoking ref/cite completions.

The basic idea is to help you insert labels in `\ref{}` commands and bibtex keys in `\cite{}` commands. The appropriate key combination shows a list of available labels or keys, and you can easily select the appropriate one. Full filtering facilities are provided. 

**Notes**: 

1. In order to find all applicable labels and bibtex keys, the plugin looks at the **saved** file. So, if you invoke this command and do not see the label or key you just entered, perhaps you haven't saved the file.

2. Only bibliographies in external `.bib` files are supported: no `\bibitem...`. Sorry. It's hard as it is. 

3. Multi-file documents are fully supported.

Now for the details. (Many of these features were contributed by Wes Campaigne and jlewegie, whom I thank profusely.)

By default, as soon as you type, for example, `\ref{` or `\cite{`, a quick panel is shown (this is the fancy drop-down list ST displays at the top of the screen), listing, respectively, all the labels in your files, or all the entries in the bibliographies you reference your file(s) using the `\bibliography{}` command. This is the default *auto-trigger* behavior, and it can be a big time saver. You can, however, turn it off, either temporarily using a toggle, or permanently by way of preference settings: see below. Once the quick panel is shown, you can narrow down the entries shown by typing a few characters. As with any ST quick panel, what you type will be fuzzy-matched against the label names or, for citations, the content of the first displayed line in each entry (by default, the author names, year of publication, short title and citation key: see below). This is *wildly* convenient, and one of the best ST features: try it!

If auto-triggering is off, when you type e.g. `\ref{`, ST helpfully provides the closing brace, leaving your cursor between the two braces. Now, you need to type `C-l,x` to get the quick panel  showing all labels in the current file. You can also type e.g. `\ref{aa` [again, the closing brace is provided by ST], then `C-l, x`, and LaTeXTools will show a list of labels that fuzzy-match the string `aa`. 

In either case, you then select the label you want, hit Return, and LaTeXTools inserts the **full ref command**, as in `\ref{my-label}`. The LaTeX command `\eqref` works the same way.  Citations from bibtex files are also supported in a similar way. Use `\cite{}`,  `\citet{}`,  `\citeyear{}` etc.

One often needs to enter **multiple citations**, as e.g. in `\cite{paper1,paper2}`. This is easy to do: either cite the first paper, e.g. `\cite{paper1}` and then, *with your cursor immediately before the right brace*, type a comma (`,`). Again, the default auto-trigger behavior is that the quick panel with appear, and you can select the second paper. If auto-trigger is off, then you enter the comma, then use the shortcut `C-l,x` to bring up the quick panel (note: you *must* add the comma before invoking the shortcut, or you won't get the intended result). Of course, you can enter as many citations as you want.

The display of bibliographic entries is *customizable*. There is a setting, `cite-panel-format`, that controls exactly what to display in each of the two lines each entry gets in the citation quick panel. Options include author, title, short title, year, bibtex key, and journal. This is useful because people may prefer to use different strategies to refer to papers---author-year, short title-year, bibtex key (!), etc. Since only the first line in each quick panel entry is searchable, how you present the information matters. The default should be useful for most people; if you wish to change the format, check the `LaTeXTools.sublime-settings` file for detailed information. (As usual, copy that file to the `User` directory and edit your copy, not the original). s

Thanks to recent contributed code, **multi-file documents** are *fully supported*. LaTeXTools looks for references, as well as `\bibliography{}` commands, in the root file and in all recursively included files. Please see the information on **multi-file documents** in the section on [**Compiling LaTeX Files**](#compiling-latex-files) for details on how to setup multi-file documents

LaTeXTools now also looks `\addbibresource{}` commands, which provides basic compatibility with biblatex.

### Toggle auto trigger mode on/off ###

**Keybinding:** `C-l,t,a,r` for references; `C-l,t,a,c` for citations

These toggles work just like the sync and focus toggles above. Indeed, `C-l,t,?` will now also display the status of the auto trigger toggles. Check the status bar for feedback (i.e. to see what the current state of the toggle is), but remember the message stays on for only a few seconds. `C-l,t,?` is your friend.



### Old-style, deprecated functionality ###

**For now**, completions are also injected into the standard ST autocompletion system. Thus, if you hit `Ctrl-space` immediately after typing, e.g., `\ref{}`, you get a drop-down menu at the current cursor position (not a quick-panel) showing all labels in your document. However, the width of this menu is OK for (most) labels, but not really for paper titles. In other words, it is workable for references, but not really for citations. Furthermore, there are other limitations dictated by the ST autocompletion system. So, this is **deprecated**, and I encourage you to use auto-trigger mode or the `C-l,x` or `C-l,C-f` keybindings instead.


Fill Helper: filling in package and file names automatically
---------------------------------------------------------

**Keybinding:** *autotriggered* by default (see below). Otherwise, `C-l,C-f`.

Thanks to the amazing work by users btstream and Ian Bacher, LaTeXTools now offers a list of available files and packages when using commands such as `\usepackage`, `\include`, `\includegraphics`, `\includesvg` and `\input`. Assuming autocompletion is toggled on (the default):

* when you type `\usepackage{`, a list of available package is displayed in the ST drop-down menu. Pick the one you need, and it will be inserted in your file, with a closing brace.

* when you type any of the file-related input commands, a list of files in the current directory is displayed (suitably filtered, so graphics files are displayed for `\includegraphics`).

To toggle autocompletion on or off, use the `fill_auto_trigger` setting, or the `c-l,t,a,f` toggle.

In order for package autocomplete to work, you need to create a cache first. You can do it using the Command Palette: select `LaTeXtools: Build cache for LaTeX packages`.

The `C-l,C-f` keyboard shortcut also works for `\ref` and `\cite` completion. Basically, wherever you can use `C-l,x`, you can also use `C-l,C-f`. 




Jumping to sections and labels
------------------------------

**Keybinding:** `C-r` (standard ST keybinding)

The LaTeXtools plugin integrates with the awesome ST "Goto Anything" facility. Hit `C-r`to get a list of all section headings, and all labels. You can filter by typing a few initial letters. Note that section headings are preceded by the letter "S", and labels by "L"; so, if you only want section headings, type "S" when the drop-down list appears.

Selecting any entry in the list will take you to the corresponding place in the text.


Jumping to included files
-------------------------

**Keybinding:** `C-l, C-o` (only works if the cursor is in the same line as the include command)

__LaTeX files__
To open a LaTeX file, which is included with `\input`, `\include` or `\subfile` just position the cursor inside the include command and press `C-l, C-o`. This will open the included file in Sublime Text.

If necessary missing folders and the file will be created. In this case the magic root entry will be written into the file. Hence this command can be used to comfortably create files and open files.

__Image files__
To open an image, which is included with `\includegraphics` just position the cursor inside the command and press `C-l, C-o`. This will open the image.
The program to open the image can be configured in the LaTeXTools settings in the `open_image_command` attribute.

The following settings are provided:

- `image_types`: a list of the image file types used in the `\includegraphics` command. This list is also used in the Fill Helper and to determine missing extensions to open images. When opening an image the `image_types`-list will be matched from left to right.
- `open_image_command`: the command/program to open an image used in the `\includegraphics` command. This commands can be configured OS-specific. For each OS you can create a list, which will be searched top-down for the matching extension. Each entry in the list has a `command` and `extension` field. The command is a string and will be executed with the file path appended, if the extension matches the extension of the file. You can optionally use `$file` inside the string to insert the file path at an arbitrary position. The `extension` can either be a string or a list of string. If it is missing, the command will be executed for every file type.


LaTeX commands and environments
-------------------------------

**Keybindings:** `C-l,c` for commands and `C-l,e` for environments

To insert a LaTeX command such as `\color{}` or similar, type the command without backslash (i.e. `color`), then hit `C-l,c`. This will replace e.g. `color` with `\color{}` and place the cursor between the braces. Type the argument of the command, then hit Tab to exit the braces.

Similarly, typing `C-l,e` gives you an environment: e.g. `test` becomes

	\begin{test}

	\end{test}

and the cursor is placed inside the environment thus created. Again, Tab exits the environment. 

Note that all these commands are undoable: thus, if e.g. you accidentally hit `C-l,c` but you really meant `C-l,e`, a quick `C-z`, followed by `C-l,e`, will fix things.


Wrapping existing text in commands and environments
---------------------------------------------------

**Keybindings:** `C-l,C-c`, `C-l, C-n`, etc.

The tab-triggered functionality just described is mostly useful if you are creating a command or environment from scratch. However, you sometimes have existing text, and just want to apply some formatting to it via a LaTeX command or environment, such as `\emph` or `\begin{theorem}...\end{theorem}`.

LaTeXTools' wrapping facility helps you in just these circumstances. All commands below are activated via a key binding, and *require some text to be selected first*. Also, as a mnemonic aid, *all wrapping commands involve typing `C-l,C-something` (which you can achieve by just holding the `C-` key down after typing `l`).

- `C-l,C-c` wraps the selected text in a LaTeX command structure. If the currently selected text is `blah`, you get `\cmd{blah}`, and the letters `cmd` are highlighted. Replace them with whatever you want, then hit Tab: the cursor will move to the end of the command.
- `C-l,C-e` gives you `\emph{blah}`, and the cursor moves to the end of the command.
- `C-l,C-b` gives you `\textbf{blah}`
- `C-l,C-u` gives you `\underline{blah}`
- `C-l,C-t` gives you `\texttt{blah}`
- `C-l,C-n` wraps the selected text in a LaTeX environment structure. You get `\begin{env}`,`blah`, `\end{env}` on three separate lines, with `env` selected. Change `env` to whatever environment you want, then hit Tab to move to the end of the environment.


These commands also work if there is no selection. In this case, they try to do the right thing; for example, `C-l,C-e` gives `\emph{}` with the cursor between the curly braces.

You can also *change the current environment* using the `C-l,C-Shift-n` shortcut. Note well how this works. First, the cursor must be inside the environment you are interested in. Second, the command selects the environment name in the `\begin{env}` command and also in the `\end{env}` command (using ST's multiple-selection support). This way you can rename the environment as needed. *Remember to exit multiple-selection mode* when you are done by pressing the `ESC` key.


LaTeX-cwl support
-----------------

LaTeXTools automatically supports the `LaTeX-cwl` autocompletion package. If the package is installed, support is automatically enabled. By default, as soon as one types, e.g., `\te`, a popup is shown displaying possible completions, including e.g. `\textit` and the like. I personally don't use it, but many find it useful.

The following settings are provided:

* `cwl_list`: a list of paths to the `cwl` files
* `command_completion`: when to show that cwl completion popup. The possible values are:
  - `prefixed` (default): show completions only if the current word is prefixed with `\`
  - `always`: always show cwl completions
  - `never`: never display the popup
* `env_auto_trigger`: if `true`, autocomplete environment names upon typing `\begin{` or `\end{` (default: `false`)


Command completion, snippets, etc.
----------------------------------

By default, ST provides a number of snippets for LaTeX editing; the LaTeXTools plugin adds a few more. You can see what they are, and experiment, by selecting Tools|Snippets|LaTeX and Tools|Snippets|LaTeXTools from the menu.

In addition, the LaTeXTools plugin provides useful completions for both regular and math text; check out files `LaTeX.sublime-completions` and `LaTeX math.sublime-completions` in the LaTeXTools directory for details. Some of these are semi-intelligent: i.e. `bf` expands to `\textbf{}` if you are typing text, and to `\mathbf{}` if you are in math mode. Others allow you to cycle among different completions: e.g. `f` in math mode expands to `\phi` first, but if you hit Tab again you get `\varphi`; if you hit Tab a third time, you get back `\phi`.

Viewers
-------

By default, LaTeXTools supports the following viewers, depending on platform:
 * On OS X, Skim
 * On Windows, Sumatra
 * On Linux, Evince

However, there is now support for custom viewers, if not a lot of choice available at the moment (patches welcome). Currently the only non-default viewers supported are Preview on OS X and Okular on Linux. Preview can be selected by changing the `viewer` setting in your LaTeXTools preferences to `"preview"`. Okular can be used by changing the `viewer` setting in your LaTeXTools preferences to `"okular"`.

### Command Viewer ###

Some support for other viewers is provided via the `command` viewer, which allows the execution of arbitrary commands to view a pdf or perform a forward search. At the very least this provides a way to use okular.

Using the command viewer requires that you configure the command(s) to be run in the platform-specific part of the `viewer_settings` block in your LaTeXTools preferences. There are three commands available:

 * `forward_sync_command`: the command to executing a forward search (`ctrl + l, j` or `cmd + l, j`).
 * `view_command`: the command to simply view the PDF document.

Of these, on `view_command` needs to be specified, though you will not have forward search capabilities unless you specify a `forward_sync_command` as well.

The following variables will be substitued with appropriate values inside your commands:

|Variable|Description|
|--------|-----------|
|$pdf_file           | full path of PDF file, e.g. _C:\Files\document.pdf_|
|$pdf_file_name      | name of the PDF file, e.g. _document.pdf_|
|$pdf_file_ext       | extension of the PDF file, e.g. _pdf_|
|$pdf_file_base_name | name of the PDF file without the extension, e.g. _document_|
|$pdf_file_path      | full path to directory containing PDF file, e.g. _C:\Files_|
|$sublime_binary     | full path to the Sublime binary|

In addition, the following variables are available for the `forward_sync_command` only:

|Variable|Description|
|--------|-----------|
|$src_file           | full path of the tex file, e.g. _C:\Files\document.tex_|
|$src_file_name      | name of the tex file, e.g., _document.tex_|
|$src_file_ext       | extension of the tex file, e.g. _tex_|
|$src_file_base_name | name of the tex file without the extension, e.g. _document_|
|$src_file_path      | full path to directory containing tex file, e.g. _C:\Files_|
|$line               | line to sync to|
|$col                | column to sync to|

If none of these variables occur in the command string, the `$pdf_file` will be appended to the end of the command.

Commands are executed in the `$pdf_file_path`, i.e., the folder containing the `$pdf_file`.

For example, you can use the command viewer to support Okular with the following settings in your `LaTeXTools.sublime-settings` file:

```json
"viewer": "command",

"viewer_settings": {
	"linux": {
		"forward_sync_command": "okular --unique $pdf_file#src:$line$src_file",
		"view_command": "okular --unique"
	}
}
```


Support for non-`.tex` files
----------------------------

LaTeXTools has some degree of support for LaTeX documents that are in files with an extension other than `.tex`. In particular, this feature is designed to work  well with alternative extensions, such as `.ltx`. Other extensions such as `.Rnw` and `.tikz` are supported, but, for now they will be treated as standard LaTeX documents (patches are always welcome!).

This behaviour is controlled through two settings, `tex_file_exts` and `latextools_set_syntax`.

* `tex_file_exts` (`['.tex']`): a list of extensions that should be considered TeX documents. Any extensions in this list will be treated exactly the same as `.tex` files: they can serve as the TeX master file, they will be searched (if included) for labels or bibliographies, etc.
* `latextools_set_syntax` (`true`): if `true` LaTeXTools will automatically set the syntax to `LaTeX` when opening or saving any file with an extension in the `tex_file_exts` list.

Note that while the extension detection is used by features of LaTeXTools, including, other features---especially the auto-completions---depend on the syntax of the file being set to `LaTeX` as well.


Spell-checking
--------------

LaTeXTools parses the `%!TEX spellcheck` directive to set the language for the spell-checker integrated in Sublime Text. The [Dictionaries](https://github.com/titoBouzout/Dictionaries) package is recommended and supported. If you have additional dictionaries, you can add them using the `tex_spellcheck_paths` setting. This is a mapping from the locales to the dictionary paths. Each locale must be lowercase and minus (-) separated and the dictionary paths must be compatible with the Sublime Text spell-checker. For example `{"en-us": "Packages/Language - English/en_US.dic"}` would be a valid value.


Miscellaneous
-------------

You can consult the documentation for any LaTeX package by invoking the `View Package Documentation` command via the Command Palette (for now).



Settings
--------

LaTeXTools supports user-defined settings. The settings file is called `LaTeXTools.sublime-settings`. A default version resides in the LaTeXTools plugin directory and **must not be edited**. This contains default settings that will work in many cases, for standard configurations of TeX distros and PDF viewers. You can however create another settings file in your `User` directory; again, the file must be named `LaTeXTools.sublime-settings`.

You can create and edit such a file manually. It is a standard Sublime Text JSON file; the settings currently honored by LaTeXTools are listed below. However, the *simplest way to create a settings file* is to open the `Preferences | Package Settings | LaTeXTools` submenu and select the `Settings - User` option. If you do not currently have a `LaTeXTools.sublime-settings` settings file in your `User` directory (e.g., if you are installing LaTeXTools for the first time), you will be given the option to create one. The newly created settings file will be an exact copy of the default one, and will open in a tab for you to customize. 

If you *do* already have an existing `LaTeXTools.sublime-settings` file in your `User` directory, the `Settings - User` option will open that file in a tab for you to further customize. Similarly, the `Settings - Default` option will open the default settings file in a tab, in *read-only mode*. This may be useful for you to copy from, or if you want to see what other options may be available without consulting this README file.

If at any time you wish to erase your customizations and start afresh, you can simply delete the `LaTeXTools.sublime-settings` file in your `User` directory. (Again, *warning*: do *not* touch the settings file in the LaTeXTools plugin directory!) Alternatively, from the `Preferences | Package Settings | LaTeXTools` submenu, or from the Command Palette, you can choose `Reset user settings to default`. This will delete any existing settings file in `User` and create a copy of the default one. This will  *remove all your customizations*. 

(Historical note: This is no longer relevant in 2016, but just for the record, if you have a pre-2014, old-style settings file, this option will import it).

<br>

*Warning*:  in general, tweaking options can cause breakage. For instance, if on Linux you change the default `python2` setting (empty by default) to a non-existent binary, forward and inverse search will stop working. With great power comes great responsibility! If you think you have found a bug, *delete your settings file in the `User` directory, or use the `Reset user settings to default` command before reporting it!* Thanks :-)

<br>

The following options are currently available (defaults in parentheses):

**General settings**:
- `cite_auto_trigger` (`true`): if `true`, typing e.g. `\cite{` brings up the citation completion quick panel, without the need to type `C-l,x`. If `false`, you must explicitly type `C-l,x`.
- `ref_auto_trigger` (`true`): ditto, but for `\ref{` and similar reference commands
- `fill_auto_trigger` (`true`): ditto, but for package and file inclusion commands (see Fill Helper feature above)
- `cwl_completion` (`prefixed`): when to activate the cwl completion poput (see LaTeX-cwl feature above)
- `cwl_list` (empty): list of paths to cwl files
- `keep_focus` (`true`): if `true`, after compiling a tex file, ST retains the focus; if `false`, the PDF viewer gets the focus. Also note that you can *temporarily* toggle this behavior with `C-l,t,f`. **Note**: If you are on either Windows or Linux you may need to adjust the `sublime_executable` setting for this to work properly. See the **Platform settings** below.
- `forward_sync` (`true`): if `true`, after compiling a tex file, the PDF viewer is asked to sync to the position corresponding to the current cursor location in ST. You can also *temporarily* toggle this behavior with `C-l,t,s`.
- `temp_files_exts`: list of file extensions to be considered temporary, and hence deleted using the `C-l, backspace` command.
- `temp_files_ignored_folders`: subdirectories to skip when deleting temp files.
* `tex_file_exts` (`['.tex']`): a list of extensions that should be considered TeX documents. Any extensions in this list will be treated exactly the same as `.tex` files. See the section on [Support for non-`.tex` files](#support-for-non-tex-files).
* `latextools_set_syntax` (`true`): if `true` LaTeXTools will automatically set the syntax to `LaTeX` when opening or saving any file with an extension in the `tex_file_exts` list.
* `tex_spellcheck_paths` (`{}`): A mapping from the locales to the paths of the dictionaries. See the section [Spell-checking](#spell-checking)
* `hide_local_cache` (`true`): Whether the local cache should be hidden in the sublime cache path (`true`) or in the same directory as the root file (`false`). See the section [Caching](#caching).
* `local_cache_life_span` (`30 m`): The lifespan of the local cache. See the section [Caching](#caching).

**Platform settings**:
- all platforms:
  * `texpath`: the path to TeX & friends
- `windows`-specific settings:
  * `distro`: either `miktex` or `texlive`, depending on your TeX distribution
  * `sumatra`: leave blank or omit if the SumatraPDF executable is in your `PATH` and is called `SumatraPDF.exe`, as in a default installation; otherwise, specify the *full path and file name* of the SumatraPDF executable.
  * `sublime_executable`: this is used if `keep_focus` is set to true and the path to your sublime_text executable cannot be discovered automatically. It should point to the full path to your executable `sublime_text.exe`.
  * `keep_focus_delay`: this is used if `keep_focus` is set to true. It controls how long (in seconds) the delay is between the completion of the `jump_to_pdf` command and the attempt to refocus on Sublime Text. This may need to be adjusted depending on your machine or configuration.
- `linux`-specific settings:
  * `python2` (`""`, i.e. empty string): name of the Python 2 executable. This is useful for systems that ship with both Python 2 and Python 3. The forward/backward search used with Evince require Python 2.
  * `sublime` (`sublime-text`): name of the ST executable. Ubuntu supports both `sublime-text` and `subl`; other distros may vary.
  * `sync_wait` (1.5): when you ask LaTeXTools to do a forward search, and the PDF file is not yet open (for example, right after compiling a tex file for the first time), LaTeXTools first launches evince, then waits a bit for it to come up, and then it performs the forward search. This parameter controls how long LaTeXTools should wait. If you notice that your machine opens the PDF, then sits there doing nothing, and finally performs the search, you can decrease this value to 1.0 or 0.5; if instead the PDF file comes up but the forward search does not seem to happen, increase it to 2.0.
  * `sublime_executable`: this is used if `keep_focus` is set to true and the path to your sublime_text executable cannot be discovered automatically. It should point to the full path to your executable `sublime_text`.
  * `keep_focus_delay`: this is used if `keep_focus` is set to true. It controls how long (in seconds) the delay is between the completion of the `jump_to_pdf` command and the attempt to refocus on Sublime Text. This may need to be adjusted depending on your machine or configuration.

**Build engine settings**:

NOTE: for the time being, you will need to refer to the `LaTeXTools.sublime-settings` file for detailed explanations. Also, since the new build system is meant to be fully customizable, if you use a third-party builder (which hopefully will become available!), you need to refer to its documentation.
- `builder`: the builder you want to use. Leave blank (`""`) or set to `"default"` or `"traditional"` for the traditional (`latexmk`/`texify`) behavior.
- `builder_path`: builders can reside anywhere Sublime Text can access. Specify a path *relative to the Sublime text Packages directory*. In particular, `User` is a good choice. If you use a third-party builder, specify the builder-provided directory.
- `display_bad_boxes` (`false`): if `true` LaTeXTools will display any bad boxes encountered after a build. Note that this is disabled by default.
- `builder-settings`: these are builder-specific settings. For the `default`/`traditional` builder, the following settings are useful:
  * `program`: one of `pdflatex` (the default), `xelatex` or `lualatex`. This selects the TeX engine.
  * `command`: the precise `latexmk` or `texify` command to be invoked. This is specified exactly as in the `cmd` entry of the old `LaTeX.sublime-build` file (which is no longer honored): it must be a list of strings. The defaults (hardcoded, not shown in the settings file) are `["latexmk", "-cd", "-e", "$pdflatex = '%E -interaction=nonstopmode -synctex=1 %S %O'", "-f", "-pdf"]` for TeXLive, and `["texify", "-b", "-p", "--tex-option=\"--synctex=1\""]` for MiKTeX.
  * `options`: allows you to specify a TeX option, such as `--shell-escape`. This must be a tuple: that is, use `options: ["--shell-escape"]`
  * In addition, there can be platform-specific settings. An important one for Windows is `distro`, which must be set to either `miktex` or `texlive`.
  * A platform-specific setting that is common to all builders is `env`. This can be used to set environment variables *before* running the actual builder. Setting e.g. `TEXINPUTS` is a possible use case.

**Viewer settings**:

 * `viewer`: the viewer you want to use. Leave blank (`""`) or set to `"default"`for the platform-specific viewer. Can also be set to `"preview"` if you want to use Preview on OS X, `"okular"` if you want to use Okular on Linux or `"command"` to run arbitrary commands. For details on the `"command"` option, see the section of the viewer documentation above.
 * `viewer_settings`: these are viewer-specific settings. Please see the viewers documentation above.

**Bibliographic references settings**:

- `bibliography` (`"traditional_bibliography"`): specifies the bibliography plugin to use to handle extracting entries from a bibliography.
- `cite-panel-format` and `cite_autocomplete_format`: see the section on ref/cite completion, and the comments in `LaTeXTools.sublime-settings`

### Project-Specific Settings ###

The above settings can be overridden on a project-specific basis if you are using Sublime Text's project system. To override these settings, simply create a [`"settings"` section in your project file](http://docs.sublimetext.info/en/latest/file_management/file_management.html#the-sublime-project-format). The structure and format is the same as for the `LaTeXTools.sublime-settings` file. Here is an example:

	{
		...<folder-related options here>...

		"settings" : {
			"TEXroot": "main.tex",
			"tex_file_exts": [".tex", ".tikz"],
			"builder_settings": {
				"program": "xelatex",
				"options": "--shell-escape"
			}
		}
	}

This sets `main.tex` as the master tex file (assuming a multi-file project), and allows `.tikz` files to be recognized as tex files, but only for the current project. Furthermore (using the default, i.e., traditional builder), it forces the use of `xelatex` instead of the default `pdflatex`, and also adds the `--shell-escape` option---again, for the current project only.

**Note:** tweaking settings on a project-specific level can lead to even more subtle issues. If you notice a bug, in addition to resetting your `LaTeXTools.sublime-settings` file, you should remove at LaTeXTools settings from your project file.


Customizing the Build System
----------------------------

LaTeXTools allows you to fully customize the build process using Python. The default builder (called `traditional`) works like the one in prior releases. 

For minor customizations of the default builder, as noted in the Build and Settings sections above, there are three key options. If you want to use, say, `xelatex` instead of `pdflatex` (the default), set the `program` setting, under `builder-settings`. You can also pass options to the TeX engine, via the `options` setting. Alternatively, both engine and options can be specified using `%!TEX` directives at the top of your master file. If instead you want to change the build command completely, set the `command` option there. 

Some information on the new flexible builder system: to create and use a new builder, you place the code somewhere off the ST `Packages` directory (for instance, in `User`), then set the `builder` and `builder_path` options in your `LaTeXTools.sublime-settings` file accordingly. A builder can define its own options, also in `LaTeXTools.sublime-settings`, which will be passed whenever a build is invoked.

Due to time constraints, I have not yet been able to document how to write a builder. The basic idea is that you subclass the `PdfBuilder` class in the file `LaTeXTools/builders/pdfBuilder.py`. The comments in that file describe how builders interact with the build command (hint: they use Pyton's `yield` command). I provide three builders. The code is in the `LaTeXTools/builders` directory. You can use them as examples:
- `traditional` is the traditional builder. 
- `simple` does not use external tools, but invokes `pdflatex` and friends, each time checking the log file to figure out what to do next. It is a very, very simple "make" tool, but it demonstrates the back-and-forth interaction between LaTeXTools and a builder.
- `script` (see below) allows the user to specify a list of compilation commands in the settings file, and just execute them in sequence. 

Let me know if you are interested in writing a custom builder!

Script Builder
--------------

LaTeXTools now supports the long-awaited script builder. It has two primary goals: first, to support customization of simple build workflows and second, to enable LaTeXTools to integrate with external build systems in some fashion.

Note that the script builder should be considered an advanced feature. Unlike the "traditional" builder it is not designed to "just work," and is not recommend for those new to using TeX and friends. You are responsible for making sure your setup works. Please read this section carefully before using the script builder.

For the most part, the script builder works as described in the [Compiling LaTeX files](#compiling-latex-files) section *except that* instead of invoking either `texify` or `latexmk`, it invokes a user-defined series of commands. Note that although the Script Builder supports **Multi-file documents**, it does not support either the engine selection or passing other options via the `%!TEX` macros.

The script builder is controlled through two settings in the *platform-specific* part of the `builder_settings` section of `LaTeXTools.sublime-settings`, or of the current project file (if any):

- `script_commands` — the command or list of commands to run. This setting **must** have a value or you will get an error message.
- `env` — a dictionary defining any environment variables to be set for the environment the command is run in.

The `script_commands` setting should be either a string or a list. If it is a string, it represents a single command to be executed. If it is a list, it should be either a list of strings representing single commands or a list of lists, though the two may be mixed. For example:

```json
"builder_settings": {
	"osx": {
		"script_commands": "pdflatex -synctex=1 -interaction=nonstopmode"
	}
}
```

Will simply run `pdflatex` against the master document, as will:

```json
"builder_settings": {
	"osx": {
		"script_commands": ["pdflatex -synctex=1 -interaction=nonstopmode"]
	}
}
```

Or:

```json
"builder_settings": {
	"osx": {
		"script_commands": [["pdflatex", "-synctex=1 -interaction=nonstopmode"]]
	}
}
```

More interestingly, the main list can be used to supply a series of commands. For example, to use the simple pdflatex -> bibtex -> pdflatex -> pdflatex series, you can use the following settings:

```json
"builder_settings": {
	"osx": {
		"script_commands": [
			"pdflatex -synctex=1 -interaction=nonstopmode",
			"bibtex",
			"pdflatex -synctex=1 -interaction=nonstopmode",
			"pdflatex -synctex=1 -interaction=nonstopmode"
		]
	}
}
```

Note, however, that the script builder is quite unintelligent in handling such cases. It will not note any failures nor only execute the rest of the sequence if required. It will simply continue to execute commands until it hits the end of the chain of commands. This means, in the above example, it will run `bibtex` regardless of whether there are any citations.

It is especially important to ensure that, in case of errors, TeX and friends do not stop for user input. For example, if you use `pdflatex` on either TeXLive or MikTeX, pass the `-interaction=nonstopmode` option. 

Each command can use the following variables which will be expanded before it is executed:

|Variable|Description|
|--------|--------|
|`$file`   | The full path to the main file, e.g., _C:\Files\document.tex_|
|`$file_name`| The name of the main file, e.g., _document.tex_|
|`$file_ext`| The extension portion of the main file, e.g., _tex_|
|`$file_base_name`| The name portion of the main file without the, e.g., _document_|
|`$file_path`| The directory of the main file, e.g., _C:\Files_|

For example:

```json
"builder_settings": {
	"osx": {
		"script_commands": ["pdflatex -synctex=1 -interaction=nonstopmode $file_base_name"]
	}
}
```

Note that if none of these variables occur in the command string, the `$file_base_name` will be appended to the end of the command. This may mean that a wrapper script is needed if, for example, using `make`.

Commands are executed in the same path as `$file_path`, i.e. the folder containing the main document.

### Caveats ###

LaTeXTools makes some assumptions that should be adhered to or else things won't work as expected:
- the final product is a PDF which will be written in the same directory as the main file and named `$file_base_name.pdf`
- the LaTeX log will be written in the same directory as the main file and named `$file_base_name.log`
- if you change the `PATH` in the environment (by using the `env` setting), you need to ensure that the `PATH` is still sane, e.g., that it contains the path for the TeX executables and other command line resources that may be necessary.

In addition, to ensure that forward and backward sync work, you need to ensure that the `-synctex=1` flag is set for your latex command. Again, don't forget the `-interaction=nonstopmode` flag (or whatever is needed for your tex programs not to expect user input in case of error).


Caching
-------

LaTeXTools uses a cache to store relevant information about your document and improve the performance of commands. However the content of the cache might be outdated. Hence you can just clear the local cache by deleting the temp files `C-backspace` or only the cache `C-l,C-d,C-c`.
The local cache also has a lifespan, after which it will be invalidated. The lifespan starts when the first entry is inserted in the cache and the whole cache will be deleted after the lifespan. This can be set in the `local_cache_life_span` setting. The format is `"X d X h X m X s"`, where `X` is a natural number `s` stands for seconds, `m` for minutes, `h` for hours, and `d` for days. Missing fields will be treated as 0 and white-spaces are optional. Hence you can write `"1 h 30 m"` to refresh the cached data every one and a half hours. If you use `"infinite"` the cache will not be invalidated automatically. A lower lifespan will produce results, which are more up to date. However it requires more recalculations and might decrease the performance.
The cache uses files to store the entries. These files can either be stored in the same folder as the tex root file or stored "hidden" in the sublime cache path. The setting for this is `hide_local_cache` and can either be `true` or `false`.


Troubleshooting
---------------

### Path issues ###

Many LaTeXTools problems are path-related. The `LaTeX.sublime-build` file attempts to set up default path locations for MikTeX, TeXlive and MacTeX, but these are not guaranteed to cover all possibilities. Please let me know if you have any difficulties.

On Mac OS X, just having your `$PATH` set up correctly in a shell (i.e., in Terminal) does *not* guarantee that things will work when you invoke commands from ST. If something seems to work when you invoke `pdflatex` or `latexmk` from the Terminal, but building from within ST fails, you most likely have a path configuration issue. One way to test this is to launch ST from the Terminal, typing

	/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl

(and then Return; this is for ST2 of course) at the prompt. If things do work when you run ST this way, but they fail if you launch ST from the Dock or the Finder, then there is a path problem. From the Terminal, type

	echo $PATH

and take note of what you get. Then, run ST from the Dock or Finder, open the console (with ``Ctrl+ ` ``) and type
	
	import os; os.environ['PATH']

and again take note of what you see in the output panel (right above the line where you typed the above command). Finally, look at the `path` keyword in the `osx` section of the `LaTeX.sublime-build` file in the LaTeXTools package directory. For things to work, every directory that you see listed from the Terminal must be either in the list displayed when you type the `import os...` command in the ST console, or else it must be explicitly specified in `LaTeX.sublime-build`. If this is not the case, add the relevant paths in `LaTeX.sublime-build` and *please let me know*, so I can decide whether to add the path specification to the default build file. Thanks!

### Non-ASCII characters and spaces in path and file names ###

Another *significant* source of issues are **Unicode characters in path and file names**. On TeXLive-based platforms, LaTeXTools tries to handle these by telling `latexmk` to `cd` to each source file's directory before running `pdflatex`. This seems to help some. However, things seem to vary by platform and locale, so I cannot make any guarantees that your Unicode path names will work. Keep in mind that TeX itself has issues with Unicode characters in file names (as a quick Google search will confirm).

Spaces in paths and file names *are* supported. As far as I know, the only limitation has to do with multifile documents: the root document's file name cannot contain spaces, or the `%!TEX = <name>` directive will fail. I may fix this at some point, but for now it is a limitation.

### Compilation hangs on Windows ###

On Windows, sometimes a build seems to succeed, but the PDF file is not updated. This is most often the case if there is a stale pdflatex process running; a symptom is the appearence of a file with extension `.synctex.gz(busy)`. If so, launch the Task Manager and end the `pdflatex.exe` process; if you see a `perl.exe` process, end that, too. This kind of behavior is probably a bug: LaTeXTools should be able to see that something went wrong in the earlier compilation. So, *please let me know*, and provide me with as much detail as you can (ideally, with a test case). Thanks!


### Log parsing issues, and good vs. bad path/file names (again!) ###

As noted in the Highlights, the new parser is more robust and flexible than the old one---it "understands" the log file format much, much better. This is the result of *manually* and *painstakingly* debugging a fair number of users' log files. The many possible exceptions, idiosyncrasies, warts, etc. displayed by TeX packages is mind-boggling, and the parsing code reflects this :-(

Anyway, hopefully, errors should now occur only in strange edge cases. Please *let me know on github* if you see an error message. I need a log file to diagnose the problem; please upload it to gist, dropbox, or similar, and paste a link in your message on github. Issue #104 is open for that purpose.

There are *two exceptions* to this request. First, the *xypic* package is very, very badly behaved. I have spent more time debugging log files contaminated by xypic than I have spent fixing all other issues. Seriously. Therefore, first, parsing issues are now reported as "warnings" if the xypic package is used (so compilation and previewing continues); second, I cannot promise I will fix the issue even if you report it. Thanks for your understanding. 

The second exception has to do with file and path names. In order to accommodate the many possible naming conventions across platforms and packages, as well as the different ways in which file names can occur in logs, I had to make some assumptions. The key one is that *extensions cannot contain spaces*. The reason is that the regex matching file names uses a period (".") followed by non-space characters, followed by a space as denoting the end of the file name. Trust me, it's the most robust regex I could come up with. So, you can have spaces in your base names, and you can even have multiple extensions; however, you cannot have spaces in your extensions. So, "This is a file.ver-1.tex" is OK; "file.my ext" (where "my ext" is supposed to be the extension) is *not OK*.

Finally, I have done my best to accommodate non-ASCII characters in logs. I cannot promise that everything works, but I'd like to know if you see issues with this.
 
