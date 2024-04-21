  <style>
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

  <div class="login-form">
    <h2>Login</h2>
    <form method="post">
      <label for="username">Username</label>
      <input name="username" id="username" required>
      <label for="password">Password</label>
      <input type="password" name="password" id="password" required>
      <input type="submit" value="Log In">
    </form>
    <p>Don't have an account? <a href="register.svelte" target="_self">Register</a></p>
  </div>
  
  