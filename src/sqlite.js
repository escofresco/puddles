/**
 * Module handles database management
 *
 * Server API calls the methods in here to query and update the SQLite database
 */

// Utilities we need
const fs = require("fs");

// Initialize the database
const dbPuddlesFile = "./.data/puddles.db";
const puddlesExists = fs.existsSync(dbPuddlesFile);
const sqlite3 = require("sqlite3").verbose();
const dbWrapper = require("sqlite");
let dbPuddles;

/* 
We're using the sqlite wrapper so that we can make async / await connections
- https://www.npmjs.com/package/sqlite
*/
// dbWrapper
//   .open({
//     filename: dbFile,
//     driver: sqlite3.Database
//   })
//   .then(async dBase => {
//     db = dBase;

//     // We use try and catch blocks throughout to handle any database errors
//     try {
//       // The async / await syntax lets us write the db operations in a way that won't block the app
//       if (!exists) {
//         // Database doesn't exist yet - create Choices and Log tables
//         await db.run(
//           "CREATE TABLE Choices (id INTEGER PRIMARY KEY AUTOINCREMENT, language TEXT, picks INTEGER)"
//         );

//         // Add default choices to table
//         await db.run(
//           "INSERT INTO Choices (language, picks) VALUES ('HTML', 0), ('JavaScript', 0), ('CSS', 0)"
//         );

//         // Log can start empty - we'll insert a new record whenever the user chooses a poll option
//         await db.run(
//           "CREATE TABLE Log (id INTEGER PRIMARY KEY AUTOINCREMENT, choice TEXT, time STRING)"
//         );
//       } else {
//         // We have a database already - write Choices records to log for info
//         console.log(await db.all("SELECT * from Choices"));

//         //If you need to remove a table from the database use this syntax
//         //db.run("DROP TABLE Logs"); //will fail if the table doesn't exist
//       }
//     } catch (dbError) {
//       console.error(dbError);
//     }
//   });

dbWrapper
  .open({
    filename: dbPuddlesFile,
    driver: sqlite3.Database
  })
  .then(async dBase => {
    dbPuddles = dBase;

  try {
      // The async / await syntax lets us write the db operations in a way that won't block the app
      if (!puddlesExists) {
        // Database doesn't exist yet - create Puddles and Puddle tables
        await dbPuddles.run(
          "CREATE TABLE Puddles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, total REAL)"
        );

        // Log can start empty - we'll insert a new record whenever the user chooses a poll option
        await dbPuddles.run(
          "CREATE TABLE Transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, PuddleID INTEGER, name TEXT, amount TEXT, date DATE, FOREIGN KEY(PuddleID) REFERENCES Puddles(id))"
        );
        
        // Add default puddles
        // await dbPuddles.run(
        //   "INSERT INTO Puddles (title, total) VALUES ('Savings', 0.0), ('Essentials', 0.0), ('Disposable', 0.0), ('Demo', 0.0)"
        // );
        
        // Add default transactions
        await dbPuddles.run(
          "INSERT INTO Transactions (PuddleId, name, amount, date) VALUES (3, 'United Airlines', '500 USD',	'2021-07-24')"
        )
        


      } else {
        // We have a database already
        console.log(await dbPuddles.all("SELECT * from Transactions"));

        //If you need to remove a table from the database use this syntax
        // dbPuddles.run("DROP TABLE Transactions"); //will fail if the table doesn't exist
        // dbPuddles.run("DROP TABLE Puddles"); //will fail if the table doesn't exist
      }
  } catch (dbError) {
    console.log(dbError);
  }
});

// Our server script will call these methods to connect to the db
module.exports = {
  

  /**
   * Get all transactions
   *
   * Return everything in the Transactions table
   * Throw an error in case of db connection issues
   */
  getTransactions: async () => {
    try {
      return await dbPuddles.all("SELECT * from Transactions");
    } catch (dbPuddlesErr) {
      console.error(dbPuddlesErr);
    }
  },
  
  /**
   * Process a user vote
   *
   * Receive the user vote string from server
   * Add a log entry
   * Find and update the chosen option
   * Return the updated list of votes
   */
//   processVote: async vote => {
//     // Insert new Log table entry indicating the user choice and timestamp
//     try {
//       // Check the vote is valid
//       const option = await db.all(
//         "SELECT * from Choices WHERE language = ?",
//         vote
//       );
//       if (option.length > 0) {
//         // Build the user data from the front-end and the current time into the sql query
//         await db.run("INSERT INTO Log (choice, time) VALUES (?, ?)", [
//           vote,
//           new Date().toISOString()
//         ]);

//         // Update the number of times the choice has been picked by adding one to it
//         await db.run(
//           "UPDATE Choices SET picks = picks + 1 WHERE language = ?",
//           vote
//         );
//       }

//       // Return the choices so far - page will build these into a chart
//       return await db.all("SELECT * from Choices");
//     } catch (dbError) {
//       console.error(dbError);
//     }
//   },

  /**
   * Get logs
   *
   * Return choice and time fields from all records in the Log table
   */
  // getLogs: async () => {
  //   // Return most recent 20
  //   try {
  //     // Return the array of log entries to admin page
  //     return await db.all("SELECT * from Log ORDER BY time DESC LIMIT 20");
  //   } catch (dbError) {
  //     console.error(dbError);
  //   }
  // },

  /**
   * Clear logs and reset votes
   *
   * Destroy everything in Log table
   * Reset votes in Choices table to zero
   */
//   clearHistory: async () => {
//     try {
//       // Delete the logs
//       await db.run("DELETE from Log");

//       // Reset the vote numbers
//       await db.run("UPDATE Choices SET picks = 0");

//       // Return empty array
//       return [];
//     } catch (dbError) {
//       console.error(dbError);
//     }
//   }
};

