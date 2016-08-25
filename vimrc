" Colors

syntax enable

" Spaces & Tabs

set tabstop=4   " number of spaces in tab when editing

set softtabstop=4 " number of spaces insert when hit tab

set expandtab  " tabs are spaces


" UI Config

set number
" set relativenumber

set showcmd

set cursorline " hightlight current line

filetype indent on " load filetype-specific indent files

set wildmenu " visual autocomplete for command  menu

set lazyredraw " redraw screen only when we need to.

set showmatch " hightlight matching [{()}]

" Leader Shortcuts

let mapleader=","  " leader is comma
" map leader key must before where use leader key , or won't work

" jk is escap
" that's amazing
inoremap jk <esc>

" toggle gundo
" nnoremap <leader>u :GundoToggle<CR>



" Searching 

set incsearch " search as chracter are entered

set hlsearch " hightlight matches

" turn off search highlight
" vim will keep highlight matches from searches untill you either
" run a new search, or manually stop highlighting the old serch with
" :nohlsearch. and we mapped it to key binding ,<space>
nnoremap <leader><space> :nohlsearch<CR>
" TODO: key binding not worked

" ignore case when searching
set ignorecase

" Folding 

set foldenable " enable folding

set foldlevelstart=10 " open most folds by default

set foldnestmax=10  " 10 nested fold max

" space open/closes folds
nnoremap <space> za

set foldmethod=indent " fold based on indent level
" TODO : run  :help foldmethod


" Movement

" move vertically by visual line
nnoremap j gj
nnoremap k gk
"gj and gk won't skill the break line part if the line 
"is too long and show two lines

" move to beginning/end of line
" but I don't need, so I comment it

" nnoremap B ^
" nnoremap E $

" $/^ doesn't do anything

" nnoremap $ <nop>
" nnoremap ^ <nop>

" highlight last inserted text
nnoremap gV `[v`]

" 回到上次离开的位置
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif
