function promedio_3_numeros(num1, num2, num3) {
    return (num1+num2+num3)/3;}

function cuadrado(arr) {
    resp = [];
    for (let i = 0; i < arr.length; i++) {
        resp[i] = arr[i]**2;}
    return resp;}

function impuesto(venta) {
    const tasa = 0.16;
    return [venta, venta*tasa, venta * (1 + tasa)];}

function promedio_n_numeros(nums) {
    let suma = 0;

    for (let i = 0; i < nums.length; i++) {
        suma = suma + nums[i];
    }

    return suma / nums.length;
}


console.log(promedio_3_numeros(4, 7, 10));
console.log(cuadrado([1, 2, 3, 4]));
console.log(impuesto(250));
console.log(promedio_n_numeros([1, 2, 3, 4]));