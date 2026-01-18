const form = document.getElementById("rsvpForm")
const rsvpsContainer = document.getElementById("rsvps");

async function loadRsvps() {
    const response = await fetch('/rsvps')
    const rsvps = await response.json();

    rsvpsContainer.innerHTML = '';
    rsvps.forEach(rsvp => {
        const item = document.createElement("p");
        item.textContent = 'RSVP made, Name: ${rsvp.name} Email: ${rsvp.email} You should recieve a confirmation soon!'
        
    })
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();


    const name = form.elements.name.value;
    const email = form.elements.email.value;

    await fetch('/rsvps', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    });

    form.reset();
    await loadRsvps();
});

loadRsvps();