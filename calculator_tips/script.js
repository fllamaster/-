const sumByCheck = document.querySelector('.sumByCheck');
const qualityService = document.getElementById('options');
const peopleNumber = document.querySelector('.peopleNumber');
const btnCalculate = document.querySelector('.calculate');
const btnDelete = document.querySelector('.delete');
const tipsResult = document.querySelector('.value_tips');
const totalResult = document.querySelector('.value_total');


selectFunction = function () {
    let getValue = select.value;
    console.log(getValue)
};

const tipsCalculator = {
    tips: 0,
    price: 0,
    people: 0,
    quality: 0,
    total: 0,
};

btnCalculate.addEventListener('click', btnCalculateHandler);
btnDelete.addEventListener('click', btnDeleteHandler);

function btnCalculateHandler(event) {
    event.preventDefault();
    tipsCalculator.price = sumByCheck.value;
    tipsCalculator.people = peopleNumber.value;
    tipsCalculator.quality = qualityService.value;
    tipsCalculator.tips = +tipsCalculator.price / 100 * +tipsCalculator.quality / +tipsCalculator.people;
    tipsCalculator.total = +tipsCalculator.price / +tipsCalculator.people + +tipsCalculator.tips;
    tipsResult.innerHTML = `${tipsCalculator.tips}`;
    totalResult.innerHTML = `${tipsCalculator.total}`;
};

function btnDeleteHandler(event) {
    event.preventDefault();
    sumByCheck.value = null;
    peopleNumber.value = null;
}
