'use strict';
//global
let pictureFiles = document.querySelectorAll('img');
let chartEl = document.getElementById('myChart');
let ctx = chartEl.getContext('2d');
let totalRound = 0;
let pictureName = ['bag.jpg', 'banana.jpg', 'bathroom.jpg', 'boots.jpg', 'breakfast.jpg', 'bubblegum.jpg', 'chair.jpg', 'cthulhu.jpg', 'dog-duck.jpg', 'dragon.jpg', 'pen.jpg', 'pet-sweep.jpg', 'scissors.jpg', 'shark.jpg', 'sweep.jpg', 'tauntaun.jpg', 'unicorn.jpg', 'water-can.jpg', 'wine-glass.jpg'];
let allProducts = [];
//constructor that adds info needed for each product
function Product(pictureName) {
  this.clicks = 0;
  this.views = 0;
  this.id = pictureName;
  this.src = `static/assets/${pictureName}`;
}
Product.prototype.handleClick = function () {

};
for (let i = 0; i < pictureName.length; i++) {
  allProducts.push(new Product(pictureName[i]));
}



// math to assign pictures to a random index
function randomPictureGen() {
  let index = Math.floor(Math.random() * allProducts.length);
  return allProducts[index];

}
console.log(allProducts);
//render picture function
function renderPictureGen() {
  let product1 = randomPictureGen();
  let product2 = randomPictureGen();
  let product3 = randomPictureGen();
  while (product1.id === product2.id || product1.id === product3.id || product2.id === product3.id) {
    product1 = randomPictureGen();
    product2 = randomPictureGen();
    product3 = randomPictureGen();
  }

  pictureFiles[0].id = product1.id;
  pictureFiles[0].src = product1.src;
  product1.views++;
  pictureFiles[1].id = product2.id;
  pictureFiles[1].src = product2.src;
  product2.views++;
  pictureFiles[2].id = product3.id;
  pictureFiles[2].src = product3.src;
  product3.views++;
}
renderPictureGen();
// function that adds the number of clicks allowed and renders chart
function handleClick(event) {
  for (let i = 0; i < allProducts.length; i++) {
    if (event.target.id === allProducts[i].id) {
      allProducts[i].clicks++;
    }
  }
  if (totalRound > 24) {
    alert('thank you for completing our study ');
    renderChart();

  } else {
    renderPictureGen();
    totalRound++;
    console.log(totalRound);

  }


}

pictureFiles.forEach(function (img) {
  img.addEventListener('click', handleClick);
});
function renderChart() {
  // generate our click data, generate our view data
  // loop through our images
  let clicks = [];
  let views = [];

  for (let i = 0; i < allProducts.length; i++) {
    clicks.push(allProducts[i].clicks);
    views.push(allProducts[i].views);
  }
  saveStorage();
  //saves selections to local storage in a way that they JSON and JS can understand
  function saveStorage() {
    let arrayString = JSON.stringify(allProducts);
    console.log('saveStorage', arrayString);
    localStorage.setItem('save', arrayString);

  }
  function retieveSaveStorage() {
    // retrieve data from local storage
    let data = localStorage.getItem('save');
    console.log('retrieveSavedStorage', data);
    let productData = JSON.parse(data);


    allProducts = productData;
  }
  retieveSaveStorage();
  //inputted to add click and view data to chart as well as color scheme
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: pictureName,
      datasets: [{
        label: '# of Clicks',
        data: clicks,
        backgroundColor: '#04b3d5'
      }, {
        label: '# of Views',
        data: views,
        backgroundColor: '#ffcc85'
      }],
    }
  });

}