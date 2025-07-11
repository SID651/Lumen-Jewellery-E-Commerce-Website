let openshopping=document.querySelector('.shopping');
let CloseShopping=document.querySelector('.CloseShopping');
let list=document.querySelector('.list');
let listcard=document.querySelector('.listcard');
let body=document.querySelector('body')
let total=document.querySelector('.total');
let quantity=document.querySelector('.quantity');

openshopping.addEventListener('click' ,()=>{
    body.classList.add('active');
})
CloseShopping.addEventListener('click' ,()=>{
    body.classList.add('active');
})
let products= [
    {
        id: 1,
        name: 'product name 1',
        image:'static/img/stamp.jpg',
        price:40

    },
    {
        id: 2,
        name: 'product name 2',
        image:'static/img/rubber.jpg',
        price:40

    },
    {
        id:3,
        name: 'product name 3',
        image:'static/img/stamp.jpg',
        price:40

    },
    {
        id: 4,
        name: 'product name 4',
        image:'static/img/stamp.jpg',
        price:40

    },
    {
        id: 5,
        name: 'product name 1',
        image:'static/img/stamp.jpg',
        price:40

    },
    {
        id: 6,
        name: 'product name 1',
        image:'static/img/stamp.jpg',
        price:40

    },
    
    

    
];
let listCards=[];
function initApp(){
    products.forEach((value, key)=>{
        let newDiv = document.createElement('div');
        newDiv.innerHTML = `
            <img src="image/${value.image}"/>
            <div class="title">${value.name}</div>
            <div class="price">${value.price.toLocalString()}</div>}
            <button onClick="addToCard(${key})">Add To Card</button>
        `;
        list.appendChild(newDiv)
    })
}
initApp();
function addToCard(key){
    if(listCards[key]==null){
        listCards[key]=products[key];
        listCards[key].quantity=1;
    }
    reloadCard();
}
function reloadCard(){
    listCards.innerHTML='';
    let count=0;
    let totalPrice=0;
    listCards.forEach((value, key) => {
        totalPrice=totalPrice + value.price;
        count= count + value.quantity;

        if(value !=null){
             let newDiv = document.createElement('div');
        newDiv.innerHTML = `
        <div><img src="image/${value.image}"/></div>
        <div>${value.name}</div>
        <div>${value.price.toLocalString()}</div>
        <div>${value.quantity}</div>
        <div>
        <button onclick="ChangeQuantity(${key}, ${value.quantity - 1})">-</button>
        <div class="count">${value.quantity}</div>
        <button onclick="ChangeQuantity(${key}, ${value.quantity + 1})">+</button>
<div>`;
listCards.appendChild(newDiv)

        }

    }
)

total.innerText=totalPrice.toLocaleString();
quantity.innerText=count;
}