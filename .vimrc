set nocompatible              " We want the latest Vim settings/options.


so ~/.vim/plugins.vim

syntax enable

set bg=dark

set backspace=indent,eol,start         " allow backspacing over everything in insert mode
let mapleader = ','					   " The default leader is \, but a comma is much better
set enc=utf8  						   " 文件編碼加入utf8
set number
set tabstop=4
set shiftwidth=4



"-----------Visauls-------------"
colorscheme atom-dark
set t_CO=256						   "Use 256 colors. This is useful for Terminal Vim.
set guifont=Fira_code:h15
set linespace=0					   "Macvim-specific line-height.

set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R



"------------Search-------------"
set hlsearch
set incsearch		" do incremental searching


"-----------Split Management----------"
set splitbelow
set splitright

nmap <C-J> <C-W><C-J>
nmap <C-K> <C-W><C-K>
nmap <C-H> <C-W><C-H>
nmap <C-L> <C-W><C-L>


"------------Mappings------------"

"Make it easy to edit the Vimrc file."
"<cr> is for return enter"
nmap <Leader>ev :tabedit $MYVIMRC<cr>

"Make it easy to edit the Vimrc file."
nmap <Leader>ez :tabedit $MYZSHRC<cr>

"Add simple highlight removal
nmap <Leader><space> :nohlsearch<cr>

"call NERDTreeToggle
nmap <D-1> :NERDTreeToggle<cr>
nmap <c-R> :CtrlPBufTag<cr>
nmap <D-e> :CtrlPMRUFiles<cr>
"----------Auto-Commands---------"

"Automactically source the Vimrc file on save.
"autocmd! means clear out the group and start from scratch
augroup autosourcing
	autocmd!
	autocmd BufWritePost .vimrc :silent !python ~/.vim/auto_download.py 
	autocmd BufWritePost .vimrc :silent !python copy.py
	autocmd BufWritePost .vimrc source %
augroup END

" This must be first, because it changes other options as a side effect.
set nocompatible


if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file
endif
set history=50		" keep 50 lines of command line history
set ruler		" show the cursor position all the time
set showcmd		" display incomplete commands


" In many terminal emulators the mouse works just fine, thus enable it.
if has('mouse')
  set mouse=a
endif


" Convenient command to see the difference between the current buffer and the
" file it was loaded from, thus the changes you made.
" Only define it when not defined already.
if !exists(":DiffOrig")
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis
		  \ | wincmd p | diffthis
endif
