"use strict";

const BASE_URL = "http://127.0.0.1:5000"

const listSection = document.querySelector(".cupcakes-list");
const cupcakeForm = document.querySelector("#cupcake-form");
const ul = document.createElement("ul");
listSection.append(ul);

async function makeList() {
  const res = await axios.get(`${BASE_URL}/api/cupcakes`);
  for (let cupcake of res.data.cupcakes) {
    const li = document.createElement("li");
    li.innerText = `Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}/10.0`;
    ul.append(li);
  }
}

makeList();

async function addCupcake() {
    const cupcake = {};
    cupcake.flavor = document.querySelector("#flavor").value;
    cupcake.size = document.querySelector("#size").value;
    cupcake.rating = document.querySelector("#rating").value;
    cupcake.image = document.querySelector("#image").value;
    await axios.post(`${BASE_URL}/api/cupcakes`, cupcake);
    const li = document.createElement("li");
    li.innerText = `Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}/10.0`;
    ul.append(li);
}

cupcakeForm.addEventListener("submit", (e) => {
  e.preventDefault();
  addCupcake();
});
