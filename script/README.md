# Search icons

A simple CLI app to easily find the desired icon.

> [!WARNING]
> Early stages of development!

## Checklist:

- [ ] Search algorithms:
    - [x] Simple, exact match search.
    - [ ] Search for multiple words.
    - [ ] Fuzzy search:
        - [x] Basic fuzzy search (letters must be in order, but do not need to be contiguous).
        Maybe that's all we need.
        - [ ] Advanced fuzzy search _(Do we need a better fuzzy search? I don't know. I don't know
        much about fuzzy search algorithms. I will investigate!)_.
            - Should we use an external command _(i.e. `fzf`)_?
        - [ ] Sorting results according to "rules". Obviously, full matches first, but then what?
- [ ] Highlight matches:
    - [x] Basic highlighting: It works great for exact matches, not so great with fuzzy search.
    - [ ] Make it work with fuzzy matches.
- [ ] Copy selection:
    - [ ] Copy icon:
        - [ ] Linux
            - [ ] Xorg
            - [ ] Wayland
        - [x] mac
        - [ ] windows
        - [ ] Other?
    - [ ] Copy Unicode hex number:
        - [ ] Linux
            - [ ] Xorg
            - [ ] Wayland
        - [ ] mac
        - [ ] windows
        - [ ] Other?
- [ ] Help:
    - [ ] Show initial help message/usage.
    - [ ] Command mode _(maybe with ":")_.
        - [ ] Use different colours according to modes _(i.e. green=search, purple=cmd, etc)._
        - [ ] Change top title/message according to selected mode:
            - `Search (+optional icon)`
            - `Command`
            - `...`
- [ ] Navigation:
    - [ ] Allow to select next/previous element in list of results _(it's kinda working but needs
    improvement)._
    - [ ] Scroll page up/down if the list of results occupies more than the available space.
- [ ] Control/keybindings:
    - [ ] Use familiar key bindings:
        - Type to search.
        - \<C-n> next element on the list.
        - \<C-p> previous element on the list.
        - \<ESC> Exit? _(maybe \<C-c>)_.
        - `:` Enter `command` mode (?).
        - \<C-u> Clear search _(kill line backwards)._
            - \<C-u> will conflict with `page up`?
            - \<C-d> for page down?
        - `/` Back to `search` mode.
            - What should the default mode be (when the app starts)? I think that it should start in
            search mode. I may change my mind later...
        - \<Enter> Copies selection to clipboard.
            - Another keybinding for `copy`? _(Keep reading)_
        - ...
        - I'm thinking about using lowercase letters for search, and capital letters and some symbols
        will trigger a command i.e. **Y** for `copy`, **U** for `copy Unicode`, `:` enters command
        mode, `/` enters search mode, etc. This may work since we won't perform a case sensitive 
        search, and the app doesn't require a lot of commands _(just the necessary functionality to
        find and copy an icon)._
    - [ ] Emacs/Vim keybindings? (I mean both).
    - [ ] Support arrow keys, pageUp, pageDown, Home, etc.
        - _Not strictly necessary_ since most terminal users will be familiar with **Emacs/Vim** 
        keybindings.
    - [ ] Mouse support.
        - Same point as before. Besides the terminal already provides it _(i.e. if you select with
        the mouse, it will copy to clipboard)._
- [ ] Display options:
    - [ ] List:
        - [x] Name, Icon
        - [ ] Name, Unicode, Icon
        - [ ] Unicode, Icon
        - [ ] One, two or more columns.
    - [ ] Grid:
        - [ ] Only icons
        - [ ] Icons, Unicode
        - [ ] Icons, Unicode and maybe the name (vertical)
        - [ ] Size of the grid.
- Modes:
    - [ ] Allow some setting from CLI args (i.e. `./main.py --fuzzy`).
    - [ ] Allow to select those setting also from the UI via _commands_.
    - [x] Search (default) mode.
    - [ ] Command mode:
        - [ ] List available commands.
        - [ ] Show help.
        - [ ] Select search algorithm (i.e. exact, fuzzy, grep, other).
            - I've just realised I could've use grep :stuck_out_tongue:
        - [ ] Select/toggle display options.
- Colours:
    - [ ] Terminal (16) colours _(Should be the default?)_.
    - [ ] Terminal (256) colours _(Default bg, dark bg, light bg?)_.
    - [ ] Custom palette (Truecolor).
    - [ ] Check for support? See next item _Check dependencies_.
- [ ] Check dependencies:
    - [ ] For some commands (i.e. `copy`) we may depend on certain tools to be installed oh the target
    system _(i.e. `pbcopy` on mac or `xclip` on Linux)_. Check for the binary. If not present, offer
    a solution _("Dependency not met. `xxx` needs to be installed." or "`pbcopy` not found, but you
    can still copy the text from the screen", etc)_.
    - Add here a list of dependencies:
    - [ ] pbcopy
    - [ ] xclip
    - ...
    - [ ] Check for colour support? Maybe (I haven't found a terminal that doesn't support Truecolor
    in a while).


> [!NOTE]
> **One big file?**
>
> For now I'm splitting the program in little modules. I like that. But it will make no difference
> to the user if we put everything in just one big file. It won't be so big after all _(except maybe
> for the list of icons...)_.

> [!TIP]
> **One executable?**
>
> Once most things are sorted out, we _(and by "we" I mean "I")_ can rewrite it in C++/C, Rust or Go
> and provide the source code and the binary.
