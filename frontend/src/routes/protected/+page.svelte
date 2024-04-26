<script>
    import { goto } from "$app/navigation";
    import {PUBLIC_API_URL} from "$env/static/public";
    let res = fetch(`${PUBLIC_API_URL}/check-session`, { credentials: "include" });
    if (res.ok){
        console.log("Sve ok");
    }
    else{
        alert("You are not logged in");
        goto("/login");
    }
</script>