
// function f(m){
//     for(let i=0;i<content.length;i++){
//         content[i].style.display="none"
//     }
//     content[m.selectedIndex].style.display="block"
    
// }

let selectHeader=document.querySelector(".select__header")
let selectItem=document.querySelectorAll(".select__item")
let content=document.querySelectorAll("#service__info");
content[0].classList.add("active")
document.querySelector('.select__current').innerHTML=selectItem[0].innerHTML
selectHeader.addEventListener("click",function(){
    this.parentElement.classList.toggle("active")
    
})

// let body = document.querySelector("body")
// body.addEventListener("click",function(){
//     selectHeader.parentElement.classList.remove("active")
// })


for(let i=0;i<selectItem.length;i++){
    selectItem[i].addEventListener("click",function(){
        let text=this.innerText,
        currentText=this.closest("#select").querySelector(".select__current")
        currentText.innerText=text
        this.closest("#select").classList.remove("active")
        content.forEach(item =>{
            item.classList.remove("active")
        })
        content[i].classList.add("active")
    })
}
    


  


