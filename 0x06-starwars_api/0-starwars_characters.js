#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');

// Convert the request function to a promise-based version
const requestPromise = promisify(request);

// Function to fetch character details asynchronously
async function fetchCharacterDetails (characterUrl) {
  try {
    const response = await requestPromise(characterUrl);
    const character = JSON.parse(response.body);
    console.log(character.name);
  } catch (error) {
    console.error('Error fetching character:', error);
  }
}

// Function to fetch movie details and character names
async function fetchMovieDetails () {
  try {
    const response = await requestPromise(`https://swapi.dev/api/films/${movieId}/`);
    const movie = JSON.parse(response.body);
    const characters = movie.characters;

    // Fetch character details in order
    for (const characterUrl of characters) {
      await fetchCharacterDetails(characterUrl);
    }
  } catch (error) {
    console.error('Error fetching movie:', error);
  }
}

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Invoke the main function
fetchMovieDetails();
