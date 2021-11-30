
const mru = () => {
	const vx = parseInt(document.getElementById('vx').value);
	const dt = parseInt(document.getElementById('dt').value);
    // Nuestras variables
    let d = vx * dt;
    let canvas, ctx, x, t,arr;
    // Obtenemos una referencia al canvas
    canvas = document.getElementById('canvas');
    // Y a su "contexto 2d"
    ctx = canvas.getContext('2d');
    // Generamos las coordenadas iniciales
    x = 0;
    t = 0;
    arr = [];
    // Los frames seran renderizados por este intervalo
    // aproximadamente a 24 frames por segundo (fps)
    const interval = setInterval(() => {
        // Limpiamos el canvas, eliminando el contenido
        // desde el punto (0, 0) al punto (100, 100)
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Generamos nuevas coordenadas
        // Que basicamente representan un desplazamiento lineal
        x = x >= d ? points(arr) : (vx * t);
        arr.push({x,y:canvas.height/2})
        t += 0.016666667;
        console.log(x)

        // Y dibujamos nuevamente
        ctx.fillRect(x, canvas.height / 2, 10, 10);

    }, 1000 / 60);

    const points = (arr) => {
        clearInterval(interval)
        let p = 0;
        for (let i of arr) {
            if (p % 60 == 0) {
                ctx.beginPath();
                ctx.fillRect(i.x, i.y, 10, 10);
            }
            p++;
        }
        ctx.beginPath();
        ctx.fillRect(arr[arr.length - 1].x, arr[arr.length - 1].y, 10,10);

    };
}


const parabolico = () => {
	const grados = parseInt(document.getElementById('grados').value);
	const vo = parseInt(document.getElementById('vo').value);
	
    // Nuestras variables
    const g = 9.8;


    let radian = grados * Math.PI / 180;

    let vx = vo * Math.cos(radian);
    let vy = vo * Math.sin(radian);

    let d = (Math.pow(vo, 2) * Math.sin(2 * radian)) / g;

    let canvas, ctx, x, y, t, vector;
    let tTotal = (2 * vy) / g;
    // Obtenemos una referencia al canvas
    canvas = document.getElementById('canvas');
    // Y a su "contexto 2d"
    ctx = canvas.getContext('2d');
    cty = canvas.getContext('2d');
    // Generamos las coordenadas iniciales
    x = 0;
    y = 0;
    t = 0;
    // Los frames seran renderizados por este intervalo
    // aproximadamente a 24 frames por segundo (fps)
    arr = []

    const interval = setInterval(() => {
        // Limpiamos el canvas, eliminando el contenido
        // desde el punto (0, 0) al punto (100, 100)
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Generamos nuevas coordenadas
        // Que basicamente representan un desplazamiento lineal
        x = x >= d + 30 ? points(arr) : 30 + (t * vx);
        y = (450 - (vy * t) + ((g * Math.pow(t, 2)) / 2));
        arr.push({
            x,
            y
        })
        t += 0.016666667;

        // Y dibujamos nuevamente
        ctx.beginPath();
        ctx.arc(x, y, 10, 0, 2 * Math.PI);
        ctx.stroke();
    }, 1000 / 60);

    const points = (arr) => {
        clearInterval(interval)
        let p = 0;
        for (let i of arr) {
            if (p % 60 == 0) {
                ctx.beginPath();
                ctx.arc(i.x, i.y, 4, 0, 2 * Math.PI);
                ctx.stroke();
                ctx.fill();
            }
            p++;
        }
        ctx.beginPath();
        ctx.arc(arr[arr.length - 1].x, arr[arr.length - 1].y, 10, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();

    };
}
console.log("hola");