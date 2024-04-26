import { writable } from "svelte/store";

export const user = writable({});

export const pass = writable({});


export const store = writable(null);

let sessions = []

export const getUserDetails = async ( username, password ) => {
	if ( username === user && password === pass )
		return 1
}