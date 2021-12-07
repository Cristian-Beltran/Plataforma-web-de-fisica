const mru = () => {
    const vx = parseFloat(document.getElementById('vx').value);
    const dt = parseFloat(document.getElementById('dt').value);
    const img = document.getElementById('car');
    let canvas = document.getElementById('canvas');
    const simulate = new MRU({
        vx,
        dt,
        canvas,
        size: 10,
        x0: 40,
        y0: (canvas.height * 3.3) / 4,
        img
    })
    simulate.run();
}

const parabolic = () => {
    const grados = parseFloat(document.getElementById('grados').value);
    const vo = parseFloat(document.getElementById('vo').value);
    const h = parseFloat(document.getElementById('h').value);
    const img = document.getElementById('rana');
    const imgTree = document.getElementById('tree');
    let canvas = document.getElementById('canvas');
    const simulate = new Parabolic({
        grados,
        vo,
        canvas,
        size: 10,
        x0: 40,
        y0: h,
        img,
        imgTree
    })
    simulate.run();
}

class MRU {
    constructor(data) {
        this.vx = data.vx;
        this.dt = data.dt;
        this.d = this.vx * this.dt;
        this.canvas = data.canvas;
        this.ctx = this.canvas.getContext("2d");
        this.x = 0;
        this.y = 0;
        this.t = 0;
        this.x0 = data.x0;
        this.y0 = data.y0;
        this.size = data.size;
        this.arr = [];
        this.img = data.img
    }
    run = () => {
        const interval = setInterval(() => {
            this.clear();
            if (this.x >= this.d) {
                clearInterval(interval);
                this.points();
            } else {
                this.x = (this.vx * this.t);
            }
            this.y = this.y0;
            this.arr.push({
                x: this.x,
                y: this.y
            });
            this.t += 0.016666667;
            this.paintimg(this.x, this.y)
        }, 1000 / 60)
    };
    clear = () => this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    paint = (x, y, size) => {
        this.ctx.beginPath();
        this.ctx.arc(x + this.x0, y, size, 0, 2 * Math.PI);
        this.ctx.fillStyle = "#C28B5E";
        this.ctx.fill();

    }
    paintimg = (x, y) => {
        this.ctx.drawImage(this.img, 0, 0, 550, 300, x + this.x0 - 20, y - 25, 80, 50);
    }
    points = () => {
        this.ctx.fillStyle = "#D9D1C4";
        this.ctx.font = "bold 16px arial";
        this.ctx.fillRect(340, 40, 130, 70);
        this.ctx.fillStyle = "#000000";
        this.ctx.fillText(`Distancia: ${this.d}`, 350, 60);
        this.ctx.fillText(`Tiempo: ${this.vx}`, 350, 80);
        this.ctx.fillText(`Velocidad: ${this.dt}`, 350, 100);
        stop();
        let p = 0;
        for (let i of this.arr) {
            if (p % 60 == 0) {this.paint(i.x, i.y, 4)}
            p++;
        }
    };
}


class Parabolic {
    constructor(data) {
        this.canvas = data.canvas;
        this.grados = data.grados;
        this.img = data.img;
        this.imgTree = data.imgTree;
        this.x0 = data.x0;
        this.y0 = this.canvas.height - data.y0;
        this.h = data.y0
        this.vo = data.vo;
        this.g = 9.8;
        this.radian = this.grados * Math.PI / 180;
        this.vx = this.vo * Math.cos(this.radian);
        this.vy = this.vo * Math.sin(this.radian);
        this.ymax = data.y0 + (Math.pow(this.vy, 2)) / (2 * this.g);
        this.tTotal = (this.vy + Math.sqrt(Math.pow(this.vy, 2) + (2 * this.g * data.y0))) / this.g;
        this.d = this.vx * this.tTotal;
        this.ctx = this.canvas.getContext("2d");
        this.x = 0;
        this.y = 0;
        this.t = 0;
        this.size = data.size;
        this.th = Math.sqrt(((2 * (this.ymax - this.h)) / this.g));
        this.arr = [];
    }
    run = () => {
        const interval = setInterval(() => {
            this.clear();
            this.tree();
            if (this.y >= this.canvas.height + 1) {
                clearInterval(interval);
                this.points();
            } else {this.y = (this.y0 - (this.vy * this.t) + ((this.g * Math.pow(this.t, 2)) / 2));}
            this.x = (this.vx * this.t);
            this.arr.push({
                x: this.x,
                y: this.y
            });
            this.t += 0.016666667;
            this.paintimg(this.x, this.y, this.t);
        }, 1000 / 60);
    }
    clear = () => this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    paint = (x, y, size) => {
        this.ctx.beginPath();
        this.ctx.arc(x + this.x0, y - 50, size, 0, 2 * Math.PI);
        this.ctx.fillStyle = "#FFFFFF";
        this.ctx.fill();
    }
    paintimg = (x, y, t) => {
        if (t < this.th) {
            this.ctx.drawImage(this.img, 190, 20, 130, 100, x + this.x0 - 20, y - 50 - 20, 50, 40);
        } else if (t < this.tTotal) {
            this.ctx.drawImage(this.img, 76, 150, 150, 200, x + this.x0 - 20, y - 50 - 20, 60, 50);
        } else {
            this.ctx.drawImage(this.img, 10, 30, 90, 100, x + this.x0 - 20, y - 50 - 20, 50, 40);
        }
    }
    tree = () => {
        this.ctx.drawImage(this.imgTree, 0, 0, 800, 100, 20, this.y0 - 40, 150, this.h, );
    }
    points = () => {
        this.tree();
        let p = 0;
        this.ctx.fillStyle = "#D9D1C4";
        this.ctx.font = "bold 16px arial";
        this.ctx.fillRect(290, 40, 190, 110);
        this.ctx.fillStyle = "#000000";
        this.ctx.fillText(`Distancia: ${Math.round(this.d * 100) / 100}`, 300, 60);
        this.ctx.fillText(`Altura maxima: ${Math.round(this.ymax * 100) / 100}`, 300, 80);
        this.ctx.fillText(`Tiempo: ${Math.round(this.tTotal * 100) / 100}`, 300, 100);
        this.ctx.fillText(`Velocidad en x: ${Math.round(this.vx * 100) / 100}`, 300, 120);
        this.ctx.fillText(`Velocidad en y: ${Math.round(this.vy * 100) / 100}`, 300, 140);
        for (let i of this.arr) {
            if (p % 60 == 0) {this.paint(i.x, i.y, 4)}
            p++;
        }
    };

}