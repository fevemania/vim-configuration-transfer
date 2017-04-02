## vim configuration transfer
---

**Main Functionality:**

`1. Safely transfer your vim configuration from one computer to another one, With setting up Vundle manager.
   (for detail, please look for scripy.py and .vimrc)`

`2. Whenever you change the content of .vimrc under home directory, it will be Autonomously copied to .vim/.vimrc（For backup convenience)`

---
**The following file you can edit:**

`(1) .vimrc for your own settings`

`(2) .vim/plugins.vim for your favorite plugins`

---
**All You have to do is**

`Step1. python3 script.py (detail alrealy commit in script.py)`

`Step2. open vim, and type ":PluginInstall" to download your own plugins (which edit in plugins.vim)`



**Note: the .vimirc configuration is referenced from laracast Vim Mastery Tutorial**

**Note: .vimrc should show both in Home directory and .vim folder**

**Note: The key mapping corresponds to Mac Commend Key, and only MacVim can use it. Otherwise, You have to change the keymapping yourself !**

