
<script>
  import { onMount } from 'svelte';

  let message = '';

  async function startGame() {
    const response = await fetch('http://127.0.0.1:5000/startgame');
    const data = await response.json();
    message = data.status || data.error;
  }

  onMount(() => {
    startGame();
  });
</script>

<main>
  <h1>Start Game</h1>
  <p>{message}</p>
</main>
