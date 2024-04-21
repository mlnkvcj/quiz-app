<script lang="ts">
    import '../app.postcss';
    import { AppShell, AppBar } from '@skeletonlabs/skeleton';
</script>

<!-- App Shell -->
<AppShell>
    <svelte:fragment slot="header">
        <!-- App Bar -->
        <AppBar>
            <svelte:fragment slot="lead">
                <strong class="text-xl uppercase">404 NOT FOUND</strong>
            </svelte:fragment>
            <svelte:fragment slot="trail">
                <a
                    class="btn btn-md variant-ghost-tertiary"
                    target="_self"
                    rel="noreferrer"
                    href="./src/routes/auth/login.svelte"
                >
                    Login
                </a>
            </svelte:fragment>
        </AppBar>
    </svelte:fragment>
    
    <slot />
</AppShell>