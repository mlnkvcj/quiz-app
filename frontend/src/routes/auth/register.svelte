<style>
    .register-form {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      background-color: #f7f7f7;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .register-form h2 {
      margin-bottom: 20px;
      font-size: 24px;
      text-align: center;
    }
  
    .register-form label {
      display: block;
      margin-bottom: 10px;
    }
  
    .register-form input{
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
  
    .register-form input[type="submit"] {
      width: 100%;
      padding: 10px;
      background-color: #313131;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
  
    .register-form input[type="submit"]:hover {
      background-color: #45a049;
    }
  </style>

  <div class="register-form">
    <h2>Register</h2>
    <form method="post">
		<label for="username">Username</label>
		<input name="username" id="username" required>
		<label for="password">Password</label>
		<input type="password" name="password" id="password" required>
		<input type="submit" value="Register">
	  </form>
    <p>Already have an account? <a href="login.svelte" target="_self">Login</a></p>
  </div>
  
  