set fileencodings=utf-8,gbk    
set ambiwidth=double  
" 支持中文  
  
set smartindent    
set smarttab    
set expandtab    
set tabstop=4    
set softtabstop=4    
set shiftwidth=4    
set backspace=2  
set textwidth=79  
"允许退格键删除和tab操作    
  
" 启用鼠标    
set mouse=a    
    
" 启用行号    
set nu   
filetype plugin on    
autocmd FileType python set omnifunc=pythoncomplete#Complete
let g:pydiction_location='~/.vim/tools/pydiction/complete-dict' 
let Tlist_Auto_Highlight_Tag=1   
let Tlist_Auto_Open=1   
let Tlist_Auto_Update=1   
let Tlist_Display_Tag_Scope=1   
let Tlist_Exit_OnlyWindow=1   
let Tlist_Enable_Dold_Column=1   
let Tlist_File_Fold_Auto_Close=1   
let Tlist_Show_One_File=1   
let Tlist_Use_Right_Window=1   
let Tlist_Use_SingleClick=1   
nnoremap <silent> <F8> :TlistToggle<CR>  
"设定F8为taglist开关  
