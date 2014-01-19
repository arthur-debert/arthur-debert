---
layout: post
title: "How I learn to stop worrying and love VIM"
permalink: "/trane/2009/sep/19/how-i-learn-stop-worrying-and-love-vim/"
tags: [vim textmate editors]
categories: [posts]
id: 29
date: "2009-09-19 -0300"
---
In the beginning there was Eclipse, and all was good. It was feature packed and free. It was slow, but that seemed inevitable: so many features should cost something. Then I found out TextMate, and I was immediately hooked. It was fast, responsive and powerful. It could edit just any file type with great syntax highlighting and useful commands. Until one day I had a hacking session with a [friend](http://b1n.org/). He fired up VIM and boy, it seemed like magic. I was intrigued, but saw no reason to change editors, since TextMate was incredibly smooth. But then I started to edit more and more files on different boxes, mostly unixes through ssh. Since TextMate wasn't available on other systems I had to learn enough vim to get by (basically getting into insert mode, then saving and quiting), which is pretty dumb: using VIM as it was pico. The clumsiness with VIM started to bother me more and more, those edits were slow and painful. I needed to learn VIM so I could edit in any box with ease.

So my VIM journey begins. Now, after using strictly VIM for over a month, I can't picture my self using another editor. I still have much to learn, since VIM is very customizable, but I am very used to it. 

The thing is, it does have a learning curve, and that's stems from:

- VIM is unlike other editors. Being a modal editor, VIM is a different beast. You can't just type. You need to understand visual, command and insert mode. More than understand it, you must embrace it. VIM makes no sense if you use it in insert mode all the time. Used in such manner, you might as well use nano or notepad. This means that very little of what you've previously learned will be of any use. Most editors behave pretty much the same: you type text and you run commands with keyboard shortcuts. Changing editor is merely a question of learning new commands / shortcuts. With VIM you'll need to learn an entire new model. It takes time until you muscle memory stops getting lost.
- VIM is too powerful, too configurable. This is both a technical reason and a cultural one. VIM is very customizable and has a long legacy. VIM is geared to power users, hard core users. Its features aren't easily discovered. Worse, the terminology, the help system is pretty intimidating for newbies. The long legacy implies that VIM will be installed pretty naked on your machine. VIM expects you to customize it heavily. If you edit on someone else's TextMate, chances are it will be almost identical to yours. Maybe they've added a couple of bundles, maybe they've changed some shortcut, but you'd be at home. Not with VIM. VIM users customize their settings so heavily, that it can be disorienting. So learning vim means also learning to customize it entirely. VIM is not a turnkey system, you have to spend some time with it making it behave as you desire.

Roughly speaking, the learning process I've followed was:

- The I-just-want-an-editor-stage. Learn to get out of it, save file, enter insert mode and edit it. This is the dumb nano stage. VIM sucks like this.
- The well-this-is-actually-nifty-stage. Go through the tutorial. [ Jonathan McPherson's tips](http://jmcpherson.org/editing.html) is a great quick starter as well. At this point you can move efficiently. This is the first steep step to mastery. This is where your muscle memory starts to abandon the modeless paradigm. When this is mastered, you find that you can edit files very quickly. Now you are hooked to VIM, and its design starts to make sense. Except now, you start to miss IDE like features. Maybe the color scheme isn't right for you. Maybe you need a syntax highlighting that is not readily available. Some shortcuts seem inefficient and hard to remember. You're ready for customization hell. 
- The customization-hell-stage. You start trying to bend VIM to your will. You understand how the customization works (vimrc, plugins, ftplugins, syntax). You start browsing [ vim's official website ](http://www.vim.org) and fiddle with plugins. You will scavenge vimrc files, trying to find neat customizations by chance. You want to make vim what you think it should be.
- The I-better-learn-how-this-thing-works stage. After some trial and error, you'll find out that it won't work. Since the combinations of settings and plugins is enormous you are bound to have conflicting mappings, settings and so on. Also, since the community is geared towards heavy users, you'll have difficulty understanding the documentation. You need to dive in, understand how the help works, the jargon, the logic things (tend) to follow. After groking the basics it gets so much easier. Now you can generate help, navigate it and best of all, make sense of it. Comfortable enough with the help system you'll find out that VIM has excellent documentation. Not only the core software, but also plugins. It's just that it takes a while to wrap your head around it. Things to understand: guimode, term mode, auto load, filetypes and the help system.
- The evangelizing stage. Now, after much messing with plugins, vimrcs and other goodies you understand that VIM is very flexible. Most things that annoyed you are easy to change. You'll have the most important IDE features you miss. You can navigate and edit many files at once easily. You want to let others now about it. It feels that after a long detour you've reached a summit, and it's beautiful from the top. Then you'll start to blog about it, let your coworkers know what's so cool about VIM.  Some people under this spell will go on useless rampages against Emacs.

Since VIM is so powerful and you can script it, there is always a lot to learn. I still feel like a newbie, but I can find my way through things, and fix most issues. VIML is not a very nice language to script in, but you can script it with Python, Perl or Ruby (as long as you compile it with such capabilities). 

While I was happy with TextMate, I'll be sticking to VIM now mainly because it's:

- Available in many platforms
- Ease to customize heavily
- Much better editing. Command mode rules.
- Faster and leaner.

I've [ written ](http://www.stimuli.com.br/trane/2009/sep/21/hello-vim-or-quitting-textmate-cold-turkey/) about the plugins that made the transition from TextMate possible.

And now the obligatory vimrc file. Enjoy:

<code class="vim">
" Arthur Debert
" http://www.stimuli.com.br

""""""""""""""""""""""""""""""""""""""
"            Appearance              "
""""""""""""""""""""""""""""""""""""""
colorscheme ir_black        " color scheme
set ruler                   " line numbers, rulers, and everything else
set number
set cursorline
set vb                      " Visual bell
set lazyredraw              " Don't update while in macro
set ttyfast                 " Improves redrawing
set titlestring=%f title    " Display filename in terminal window
set rulerformat=%l:%c ruler " Display current column/line
set showcmd                 " Show commands at bottom right
set splitbelow              " Split windows BELOW current window!
set winminheight=0          " Window minimum height
set scrolloff=8             " always have at least 8 lines before the window's bottom
"match ErrorMsg /\%>80v.\+/  " formats text longer than 80 columns
set foldcolumn=3              " 2 lines of column for fold showing, always
set foldmethod=syntax
set foldlevelstart=99

""""""""""""""""""""""""""""""""""""""
"  Search & Replace
""""""""""""""""""""""""""""""""""""""
set hlsearch   " highlight searches
set ignorecase " make searches case-insensitive, unless they contain upper-case letters:
set smartcase
set incsearch  " show the `best match so far' as search strings are typed:
set gdefault   " assume the /g flag on :s substitutions to replace all matches in a line:
set enc=utf-8  " UTF-8 Default encoding


""""""""""""""""""""""""""""""""""""""
"           General Settings         "
""""""""""""""""""""""""""""""""""""""
syntax on                                                            " syntax highlighting
filetype plugin on                                                   " enables filetype
set listchars=nbsp:¬¨¬®,eol:¬¨‚àÇ,tab:>-,extends:¬¨¬™,precedes:¬¨¬¥,trail:‚Äö√Ñ¬¢ " whitespace chars
set autoindent smartindent                                           " auto/smart indent
set expandtab                                                        " expand tabs to spaces
set smarttab                                                         " tab and backspace are smart " 
set ttyfast

"""""""""""""""""""""""""""""""""""""""
"           Menu completions          "
"""""""""""""""""""""""""""""""""""""""
set wildmode=full wildmenu                            " Command-line tab completion
set infercase                                         " AutoComplete in Vim
set completeopt=longest,menu,menuone
set wildignore+=*.o,*.obj,*.pyc,*.DS_STORE,*.db,*.swc


"""""""""""""""""""""""""""""""""""""""
"           GUI Stuff                 "
"""""""""""""""""""""""""""""""""""""""
set mousemodel=extend " Enable mouse support
set selectmode=mouse
set mousefocus
set mouse=a


"""""""""""""""""""""""""""""""""""""""
"    Keystrokes -- Moving Around      "
"""""""""""""""""""""""""""""""""""""""
"Space is so much easier than :
noremap <space> :
" have the h and l cursor keys wrap between lines (like <Space> and <BkSpc> do
" by default), and ~ covert case over line breaks; also have the cursor keys
" wrap in insert mode:
set whichwrap=h,l,~,[,]
" backspace over anything
set backspace=indent,eol,start
" Use smarte paste for preserving identation when copying and pasting
nmap <silent> ,p :SmartPaste<cr>
" Show a list of recently opend files:
nmap ,r :FuzzyFinderMruFile<cr>
" Show a list of files to be regex matched, under the current dir (a la textmate)
nmap ,f :FuzzyFinderTextMate<cr>
let Tlist_WinWidth = 50
" Task list bindings:
map <silent> ,T :TaskList<CR>
"Tag list
map <silent> ,t :Tlist<CR>
" joining lines
noremap ,j :join<cr>
" Bindings for tab switching:
" change tabs with shift tab
nnoremap <S-Tab> <C-W>w;
"" Scrolling
no J 20j
no K 20k
" List whitespace
nn <silent> ,<space> :se nolist!<cr>
" Buffer Window Focus
nn ,k       <C-W>k<C-W>_
nn ,=       <C-W>=
" Yank to all app's
no ,y !pbcopy<cr><esc>u 
" use smart paste "
nmap <silent> ,p :SmartPaste<cr>
" ,nn will toggle NERDTree on and off
nmap ,nn :NERDTreeToggle<cr>

"""""""""""""""""""""""""""""""""""""""
"           Plugins                   "
"""""""""""""""""""""""""""""""""""""""
" MiniBuffer support:
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1

" tag list :
let Tlist_Sort_Type = "name"
"""""""""""""""""""""""""""""""""""""""
"           Spelling                  "
"""""""""""""""""""""""""""""""""""""""
if v:version >= 700
  setlocal spell spelllang=en
  nmap ,ll :set spell!<CR>
  nmap ,le :set spelllang=en<CR>
  nmap ,lp :set spelllang=pt<CR>
endif
"   Correct some spelling mistakes    "
ia teh      the
ia htis     this
ia tihs     this
ia funciton function
ia fucntion function
ia funtion  function
ia retunr   return
ia reutrn   return
ia sefl     self
ia eslf     self


"""""""""""""""""""""""""""""""""""""""
"           GUI Stuff                 "
"""""""""""""""""""""""""""""""""""""""
autocmd BufRead *.json set filetype=javascript " clojure filetype:
autocmd BufRead *.as set filetype=actionscript " actionscript syntax:
autocmd BufRead *.clj set filetype=clojure     " clojure filetype:
autocmd BufRead *.mxml set filetype=mxml       " mxml files:
let mapleader=","

"""""""""""""""""""""""""""""""""""""""
"           backup options            "
"""""""""""""""""""""""""""""""""""""""
set backupdir=~/tmp,/tmp " backups (~)
set directory=~/tmp,/tmp " swap files
set backup               " enable backups


"""""""""""""""""""""""""""""""""""""""
"           Clipboard Management      "
"""""""""""""""""""""""""""""""""""""""
"" Improve Vim copy for OSX terminal
if has('gui_running')
    set mousefocus          " Mouse can control splits
endif
"Make sure paste mode is on before pasting
function! SmartPaste()
    set paste
    normal! p`[=`]
    set nopaste
endfunction
command! -bar            SmartPaste   :call SmartPaste()

</code>
