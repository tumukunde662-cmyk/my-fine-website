// rosey.js - Drag & Drop Logic
let cur = 0;
const tiles = document.querySelectorAll('.rtile');
const fileIn = document.getElementById('fileIn');

// Load saved photos from browser memory
tiles.forEach((t,i)=>{
  const s = localStorage.getItem('staug_'+i);
  if(s){
    t.querySelector('img').src = s;
    t.classList.add('has');
    t.querySelector('.hint').style.display = 'none';
  }
});

function handle(file, idx){
  if(!file ||!file.type.startsWith('image/')) return;
  const r = new FileReader();
  r.onload = e => {
    const b = tiles[idx];
    b.querySelector('img').src = e.target.result;
    b.classList.add('has');
    b.querySelector('.hint').style.display = 'none';
    localStorage.setItem('staug_'+idx, e.target.result);
  };
  r.readAsDataURL(file);
}

tiles.forEach((b,i)=>{
  b.addEventListener('click', ()=>{ cur=i; fileIn.click(); });
  b.addEventListener('dragover', e=>{ e.preventDefault(); b.classList.add('drag-over'); });
  b.addEventListener('dragleave', ()=> b.classList.remove('drag-over'));
  b.addEventListener('drop', e=>{
    e.preventDefault();
    b.classList.remove('drag-over');
    handle(e.dataTransfer.files[0], i);
  });
});

fileIn.onchange = e => {
  if(e.target.files[0]) handle(e.target.files[0], cur);
  fileIn.value = '';
};