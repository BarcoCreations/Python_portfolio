
var ocel = 7850;
var pi = 3.14159;


function getE(element) {
    return document.getElementById(element);
}

function roundNum(num, dec) {
    var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
    return result;
}

function ocelKruhova(in_d) {
    return ( pi * ocel * Math.pow(in_d/2,2) ) / 1000000;
}
function ocelKruhovaM(in_d, in_kg) {
    return (  ocelKruhova(in_d) * in_kg);
}

function ocelCtvercova(in_a) {
    return (ocel / 1000000 * (in_a * in_a));
}

function ocelCtvercovaM(in_a, in_kg) {
    return (ocelCtvercova(in_a) * in_kg);
}

function ocelPlocha(in_b,in_t) {
    return (ocel/1000000 * in_b * in_t);
}
function ocelPlochaM(in_b,in_t,in_kg) {
    return (ocelPlocha(in_b,in_t) * in_kg);
}

function ocelTrubky(in_t,in_d) {
    var d = in_d - 2 * in_t;
    return (( pi/4 * (Math.pow(in_d,2) - Math.pow(d,2)) ) * ocel) / 1000000;
}
function ocelTrubkyM(in_t,in_d,in_kg) {
    return ocelTrubky(in_t,in_d) * in_kg;
}





// tyc kruhova
function calculateCircleLength()
{
    var val_d  = getE('in_d').value;
    val_d =val_d.replace(",",".");
    var val_kg = getE('in_kg').value;
    val_kg=val_kg.replace(",",".");

    if(val_d == '' ) {}
    else
    {
        getE('out_kg_m').value = Math.round(ocelKruhova(val_d)*1000)/1000;
    }

    if(val_kg != '' )
    {getE('out_kg').value = Math.round(ocelKruhovaM(val_d,val_kg)*1000)/1000;
    }
    console.log(val_kg);
}




// tyc stvorcova
function calculateSquare()
{
    var val_a  = getE('in_a').value;
    val_a =val_a.replace(",",".");
    var val_kg = getE('in_kg1').value;
    val_kg=val_kg.replace(",",".");

    if(val_a == '' || val_kg == '') {
        getE('out_kg1').value = '';
    }
    else
    {
        getE('out_kg1_m').value = Math.round(ocelCtvercova(val_a)*1000)/1000;
        getE('out_kg1').value = Math.round(ocelCtvercovaM(val_a,val_kg)*1000)/1000;
    }

}

function calculateSquareLength()
{
    var val_a  = getE('in_a').value;
    val_a =val_a.replace(",",".");
    var val_kg = getE('in_kg1').value;
    val_kg=val_kg.replace(",",".");

    if(val_a == '' ) {
        getE('out_kg1').value = '';
    }
    else
    {
        getE('out_kg1_m').value = Math.round(ocelCtvercova(val_a)*1000)/1000;

    }
    if(val_kg != '' )
    {
        getE('out_kg1').value = Math.round(ocelCtvercovaM(val_a,val_kg)*1000)/1000;
    }
}

// tyc plocha
function calculateFlatSteel()
{
    var val_b  = getE('in_b').value;
    val_b=val_b.replace(",",".");
    var val_t  = getE('in_t').value;
    val_t=val_t.replace(",",".");
    var val_kg = getE('in_kg2').value;
    val_kg=val_kg.replace(",",".");

    if(val_b == '' || val_t == '') {
        getE('out_kg2_m').value = '';
    }
    if(val_b == '' || val_t == '' || val_kg == '') {
        getE('out_kg2').value = '';
    }
    else
    {
        getE('out_kg2_m').value = Math.round(ocelPlocha(val_b,val_t)*1000)/1000;
        getE('out_kg2').value = Math.round(ocelPlochaM(val_b,val_t,val_kg)*1000)/1000;
    }

}

function calculateFlatSteelLength()
{
    var val_b  = getE('in_b').value;
    val_b=val_b.replace(",",".");
    var val_t  = getE('in_t').value;
    val_t=val_t.replace(",",".");
    var val_kg = getE('in_kg2').value;
    val_kg=val_kg.replace(",",".");

    if(val_b == '' || val_t == '' ) {
        getE('out_kg2').value = '';
    }
    else
    {
        getE('out_kg2_m').value = Math.round(ocelPlocha(val_b,val_t)*1000)/1000;

    }
    if(val_kg != '')
    {
        getE('out_kg2').value = Math.round(ocelPlochaM(val_b,val_t,val_kg)*1000)/1000;
    }

}

// rury
function calculatePipe()
{
    var val_t  = getE('in_t2').value;
    val_t=val_t.replace(",",".");
    var val_d  = getE('in_d2').value;
    val_d=val_d.replace(",",".");
    var val_kg = getE('in_kg3').value;
    val_kg=val_kg.replace(",",".");

    if(val_t == '' || val_d == '' || val_kg == '') {
        getE('out_kg3').value = '';
        getE('out_kg3_m').value = '';
    }
    else
    {
        getE('out_kg3_m').value = Math.round(ocelTrubky(val_t,val_d)*1000)/1000;
        getE('out_kg3').value = Math.round(ocelTrubkyM(val_t,val_d,val_kg)*1000)/1000;
    }

}

function calculatePipeLength()
{
    var val_t  = (getE('in_t2').value);
    val_t=val_t.replace(",",".");
    var val_d  = (getE('in_d2').value);
    val_d=val_d.replace(",",".");
    var val_kg = getE('in_kg3').value;
    val_kg=val_kg.replace(",",".");

    if(val_t == '' || val_d == '') {
        getE('out_kg3').value = '';
        getE('out_kg3_m').value = '';
    }
    else
    {
        getE('out_kg3_m').value = Math.round(ocelTrubky(val_t,val_d)*1000)/1000;

    }
    if(val_kg != '' )
    {
        getE('out_kg3').value = Math.round(ocelTrubkyM(val_t,val_d,val_kg)*1000)/1000;
    }
}




// 6 hranna tyc - dodane
function calculate6hranna()
{
    var val_sw  = getE('sw').value;
    val_sw =val_sw.replace(",",".");

    var val_kg = getE('in_kg4').value;
    val_kg=val_kg.replace(",",".");

    var val_kg__m = getE('kg_m').value;
    val_kg__m=val_kg__m.replace(",",".");



    if (val_sw == '') {}
    else
    {
        //getE('kg_m').value = Math.round(ocelKruhova(val_d)*1000)/1000;
        getE('kg_m').value = Math.round( (((( 3*( (val_sw/Math.sqrt(3))*(val_sw/Math.sqrt(3)) ) * Math.sqrt(3) ) / 2) * ocel) / 1000000) *1000)/1000;


    }

    if (val_kg != '')
    {
        //getE('out_kg4').value = Math.round(ocelsethrannaM(val_sw,val_kg)*1000)/1000;
        getE('out_kg4').value = Math.round( (val_kg__m*val_kg)*1000)/1000;
    }

    //console.log(val_kg__m);

}