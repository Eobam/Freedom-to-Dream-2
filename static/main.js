const form = document.getElementById("rsvpForm")
const rsvpsContainer = document.getElementById("rsvps");

form.addEventListener("submit", (event) => {
    event.preventDefault();


    const name = form.elements.name.value;
    const email = form.elements.email.value;

    const item = document.createElement("p");
    item.textContent = 'test'
    rsvpsContainer.appendChild(item);

    form.reset();
})