  <style>
    *{
      color : black;
    }

    .login-form {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      background-color: #f7f7f7;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .login-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      text-align: center;
    }
  
    .login-form label {
      display: block;
      margin-bottom: 10px;
    }
  
    .login-form input{
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      color: black;
    }
  
    .login-form input[type="submit"] {
      width: 100%;
      padding: 10px;
      background-color: #313131;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
  
    .login-form input[type="submit"]:hover {
      background-color: #45a049;
    }
  </style>
<script>
    import { goto } from "$app/navigation";
  import { PUBLIC_API_URL } from "$env/static/public";
  import { store } from "$lib/stores";
  import { getUserDetails } from "$lib/stores";
  const credentials = {
    username: "",
    password: "",
  };
  const handleLogin = async () => {
    let res = await fetch(`${PUBLIC_API_URL}/auth/login`, { body: JSON.stringify(credentials), method: "POST" });
    if (res.ok){
      const user = await getUserDetails( credentials.username, credentials.password )
      console.log(user)
      $store = user;
      goto("/");
    }
    else{
      alert("Error logging in");
    }
  }
</script>
  <div class="login-form">
    <h2>Login</h2>
    <form method="post" on:submit|preventDefault={handleLogin}>
      <label for="username">Username</label>
      <input name="username" id="username" required bind:value={credentials.username}>
      <label for="password">Password</label>
      <input type="password" name="password" id="password" required bind:value={credentials.password}>
      <input type="submit" value="Log In">
    </form>
    <p>Don't have an account? <a href="/register">Register</a></p>
  </div>
  
  