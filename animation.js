const list = document.querySelector('ul');
const bubble = document.querySelector('.bubble');

list.addEventListener('click',function(event){
    const target = event.target;
    if (target.tagName === 'A'){
        const {width,left} = target.getBoundingClientRect();
        bubble.style.cssText = `width: ${width}px; left : ${left}px`; 
    }
});