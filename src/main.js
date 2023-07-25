"use strict";

// global variables
let cursors;
let currentScene = 0;
const SCALE = 0.5;
const tileSize = 30;

let config = {
  type: Phaser.AUTO,
  title: "Pokégguesser",
  scale: {
      mode: Phaser.Scale.FIT,
      autoCenter: Phaser.Scale.CENTER_BOTH,
      width: 1600,
      height: 900,
  },
  physics:{
    default: 'arcade',
    arcade:{
      fps: 240,
      gravity: {y: 1000},
      debug: false  
    }
  },
  scene: [Load]
};

let game = new Phaser.Game(config);