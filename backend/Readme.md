This folder handles all the scraping and storage of College course data 
onto a mongodb Atlas instance. The file mainScrapper.py is the main file which initilizes the scraping utilizing functions from baseScrapper.py

The data Schema is:

Course Info =
{ schoolName: String,
		courseName: string,
		CRN: int,
		year: date(year),
		term: summer/winter,
		department: ie Art Department,
		courseAttribute: ie Humanities outcome,
		description: strings,
		instructorName: string,
		registrationDeadline: date,
		time: date to date,
		days: ie TWR,
		location: string,
		dateRange: date - date,
		prerequisites: default(Open to all),
		remCapacity: int,
		estCost: int,


		//to be used later 
		schoolZipCode:int,

}






//Initial data Schema 
Course Info =
{ schoolName: String,
		courseName: string,
		CRN: int,
		year: date(year),
		term: summer/winter,
		department: ie Art Department,
		courseAttribute: ie Humanities outcome,
		description: strings,
		instructorName: string,
		registrationDeadline: date,
		time: date to date,
		days: ie TWR,
		location: string,
		dateRange: date - date,
}




