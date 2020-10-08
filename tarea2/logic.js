//Estudiante: Aaron Joel Limachi Quispe

function calculate(){
    console.log("Hola");
    let n = parseFloat(document.getElementById("n_value").value);
    let B = parseFloat(document.getElementById("B_value").value);
    let H = parseFloat(document.getElementById("H_value").value);
    let S = parseFloat(document.getElementById("S_value").value);

    let dn = parseFloat(document.getElementById("dn_value").value);
    let dB = parseFloat(document.getElementById("dB_value").value);
    let dH = parseFloat(document.getElementById("dH_value").value);
    let dS = parseFloat(document.getElementById("dS_value").value);

    let Q = (1/n)*(((B*H)**(5/3))/((B+2*H)**(2/3)))*(S**(1/2))

    let Qmax = (1/(n-dn))*((((B+dB)*(H+dH))**(5/3))/(((B-dB)+2*(H-dH))**(2/3)))*((S+dS)**(1/2))
    let Qmin = (1/(n+dn))*((((B-dB)*(H-dH))**(5/3))/(((B+dB)+2*(H+dH))**(2/3)))*((S-dS)**(1/2))

    let DH = (((B * S**(1/2)) * (5*B*(H**(2/3)) + 6*(H**(5/3))))/( 3*n*((B + 2*H)**(5/3)) ))*dH
    let DB = (( (H**(5/3))*(S**(1/2))*(B + 6*H) )/( 3 * n * ((B + 2*H)**(5/3)) )) * dB
    let DS = ((B*(H**(5/3)))/(2*n*(S**(1/2))*((B+2*H)**(2/3)) ))*dS
    let DQ = DH + DB + DS

    document.getElementById('error').innerHTML= "dQ = " + DQ;
    document.getElementById('original').innerHTML= "Q = " + Q;
    document.getElementById('sintetic').innerHTML= "Q = " + Q +" ± " + DQ;
    document.getElementById('between').innerHTML= "El valor se encuentra entre: " + Qmin + " hasta " + Qmax;
}