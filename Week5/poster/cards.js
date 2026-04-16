let cardsList = document.querySelector(".cards");

let cards = [];
cards.push({
  title: "Barnabas",
  url: "./barnabas/index.html",
});

cards.push({
  title: "Benedikta",
  url: "./benedikta/index.html",
});

cards.push({
  title: "Cid",
  url: "./cid/index.html",
});

cards.push({
  title: "Clive",
  url: "./clive/index.html",
});

cards.push({
  title: "Dion",
  url: "./dion/index.html",
});

cards.push({
  title: "Hugo",
  url: "./hugo/index.html",
});

cards.push({
  title: "Jill",
  url: "./jill/index.html",
});

cards.push({
  title: "Joshua",
  url: "./joshua/index.html",
});


// using forEach()
// Now loop through the cards and build the elements
cards.forEach((card) => {
  // Create the card container
  let cardDiv = document.createElement("div");
  cardDiv.classList.add("card");

  // Create the inner part
  let cardInner = document.createElement("div");
  cardInner.classList.add("card-inner");

  // Create the front of the card
  let cardFront = document.createElement("div");
  cardFront.classList.add("card-front");
  let heading = document.createElement("h2");
  heading.textContent = card.title;
  cardFront.appendChild(heading);

  // Create the back of the card
  let cardBack = document.createElement("div");
  cardBack.classList.add("card-back");
  let link = document.createElement("a");
  link.href = card.url;
  link.textContent = "Poster Link";
  cardBack.appendChild(link);

  // Assemble the card
  cardInner.appendChild(cardFront);
  cardInner.appendChild(cardBack);
  cardDiv.appendChild(cardInner);

  // Add the card to the list
  cardsList.appendChild(cardDiv);
});
