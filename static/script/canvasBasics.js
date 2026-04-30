// const canvas = document.getElementById("canvas_sb");
// const ctx = canvas.getContext("2d");

// const cw = canvas.width;
// const ch = canvas.height;
// // fillRect
// ctx.fillRect(20, 20, 100, 100); // x,y, width, height

// // strokeRect
// ctx.lineWidth = 5;
// ctx.strokeStyle = "green";
// ctx.strokeRect(150, 20, 100, 100);

// // clearReact
// // clears out a region on canvas
// ctx.clearRect(25, 25, 90, 90);

// // fillText()
// ctx.font = '30px Arial';
// ctx.fillText("Hello World", 0.8*cw, 0.9*ch);

// // strokeText()
// ctx.lineWidth = 1;
// ctx.strokeStyle = "blue";
// ctx.strokeText("Hello World", 0.8*cw, 0.8*ch);

// // Paths
// // To draw contours (Here a triangle)
// ctx.beginPath();
// ctx.moveTo(50, 0.1*ch);
// ctx.lineTo(150, 0.1*ch);
// ctx.lineTo(100, 0.3*ch);
// ctx.lineTo(50, 0.1*ch);
// ctx.stroke(); // To draw the line defined above
// ctx.fillStyle = "orange"
// ctx.fill(); // Can be used to fill in the defined path instead of drawing

// // Drawing another triangle
// ctx.beginPath();
// ctx.moveTo(300, 0.1*ch);
// ctx.lineTo(250, 0.3*ch);
// ctx.lineTo(350, 0.3*ch);
// ctx.lineTo(300, 0.1*ch);
// ctx.stroke();
// ctx.fillStyle = "violet";
// ctx.fill();


// // Drawing Rectangle
// ctx.beginPath();
// ctx.rect(450, 0.1*ch, 0.3*ch, 100);
// ctx.fillStyle = "purple";
// ctx.fill();

// // Arc/circles

// ctx.beginPath();
// ctx.arc(750, 0.2*ch, 0.1*ch, 0, 2*Math.PI, false);   // center coordinates: x, y, radius, startAngle, endAngle, clkw(false)/aclkw(true);  pi = Math.PI
// ctx.stroke();
// ctx.fillStyle = "beige";
// ctx.fill();

// // Bezier and quadratic curves


// // Animations

// const circle = {
//     x: 200,
//     y: 200,
//     size: 30,
//     dx: 5,
//     dy: 4
// }

// function drawCircle(){
//     ctx.clearRect(0, 0, cw, ch);
//     ctx.beginPath();
//     ctx.arc(circle.x, circle.y, circle.size, 0, Math.PI *2);
//     ctx.fillStyle = "red";
//     ctx.fill();
// }


// function update(){
//     drawCircle();
//     // change position
//     circle.x += circle.dx;
//     circle.y += circle.dy;
    
//     // collision detection with sidewalls
//     if (circle.x + circle.size > cw || circle.x - circle.size < 0){
//         circle.dx *= -1;
//     }
//     if (circle.y + circle.size > ch || circle.y - circle.size < 0){
//         circle.dy *= -1;
//     }
    
//     requestAnimationFrame(update); // Recalls update function
// }

// update();



// Moving with the help of keyboard input

// rect = {
//     x: 20,
//     y: 20,
//     width: 100,
//     height: 50,
//     dx: 0,
//     dy: 0,
// }

// function drawRect(){
//     ctx.fillStyle = "blue";
//     ctx.fillRect(rect.x, rect.y, rect.width, rect.height);
// }

// function newPos(){
//     rect.x += rect.dx;
//     rect.y += rect.dy
// }

// function kd(e){
//     if(e.key == "ArrowDown"){
//         e.view.event.preventDefault();     // Prevents scrolling when pressed
//         rect.dy = 4;
//     }
//     else if(e.key == "ArrowUp"){
//         e.view.event.preventDefault();     // Prevents scrolling when pressed
//         rect.dy = -4;
//     }
//     else if(e.key == "ArrowRight"){
//         rect.dx = 4;
//     }
//     else if(e.key == "ArrowLeft"){
//         rect.dx = -4;
//     }

//     newPos();
// }

// function ku(e){
//     if(e.key == "ArrowDown"){
//         rect.dy = 0;
//     }
//     else if(e.key == "ArrowUp"){
//         rect.dy = 0;
//     }
//     else if(e.key == "ArrowRight"){
//         rect.dx = 0;
//     }
//     else if(e.key == "ArrowLeft"){
//         rect.dx = 0;
//     }
// }

// function update(){
//     ctx.clearRect(0, 0, cw, ch);
//     drawRect();
//     requestAnimationFrame(update);
// }

// document.addEventListener('keydown', kd);
// document.addEventListener('keyup', ku)
// update();