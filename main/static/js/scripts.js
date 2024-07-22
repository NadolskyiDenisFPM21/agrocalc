
const varForm = document.getElementById('var-form');
const constForm = document.getElementById('const-form');



function switchForm(thisB, otherB) {
    thisB.disabled = true;
    document.getElementById(otherB).disabled = false;
    varForm.style.display = otherB == 'varB' ? 'none' : 'block';
    constForm.style.display = otherB != 'varB' ? 'none' : 'block';
}