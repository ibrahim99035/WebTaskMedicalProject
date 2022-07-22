//spans
let heartSpan = document.querySelector('#heart');
let diapSpan  = document.querySelector('#diap');
let surgSpan  = document.querySelector('#surg');
let CoronaSpan = document.querySelector('#coronaSpan');
let KidenySpan = document.querySelector('#KidneySpan')
let coronaInOutSpan = document.querySelector('#CoronaInOut')
let BrainTumourSpan = document.querySelector('#brainTumourSpan')
let anemiaSpan = document.querySelector('#anemiaSpan')
let hepSpan = document.querySelector('#hepSpan')
let BreastSpan = document.querySelector('#BreastSpan')


//divs
let heartDiv  = document.querySelector('#heartPred');
let diapDiv  = document.querySelector('#diapetes');
let surgDiv  = document.querySelector('#surgical');
let defult = document.querySelector('#default');
let coronaDiv = document.querySelector('#corona');
let kidneyDiv = document.querySelector('#KidneyDiv')
let coronaInOutDiv = document.querySelector('#coronaInOutDiv')
let BrainTumourDiv = document.querySelector('#braintumourDiv')
let AnemiaDiv = document.querySelector('#AnemiaDiv')
let HepPredictionDiv = document.querySelector('#HepPredictionDiv')
let BreastDivForm = document.querySelector('#BreastDivForm')




//events
heartSpan.addEventListener('click', () => {
    heartDiv.style.display = "block";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    HepPredictionDiv.style.display = "none";
    treatment.style.display = "none";
    AnemiaDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});

diapSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "block";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    HepPredictionDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});


surgSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "block";
    defult.style.display = "none";
    HepPredictionDiv.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    BreastDivForm.style.display = "none";
    AnemiaDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});


CoronaSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaInOutDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    coronaDiv.style.display = "block";
    BreastDivForm.style.display = "none";
    HepPredictionDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
});

KidenySpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    HepPredictionDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    coronaDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    kidneyDiv.style.display = "block";
    BrainTumourDiv.style.display = "none";
});

coronaInOutSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    HepPredictionDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    coronaInOutDiv.style.display = "block";
    BrainTumourDiv.style.display = "none";
})


BrainTumourSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    HepPredictionDiv.style.display = "none";
    treatment.style.display = "none";
    AnemiaDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    coronaInOutDiv.style.display = "none";
    BrainTumourDiv.style.display = "block";
});

anemiaSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    HepPredictionDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    BrainTumourDiv.style.display = "none";
    AnemiaDiv.style.display = "block";
});

hepSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    BreastDivForm.style.display = "none";
    BrainTumourDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    HepPredictionDiv.style.display = "block";
});

BreastSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    HepPredictionDiv.style.display = "none";
    AnemiaDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    BreastDivForm.style.display = "block";
});
