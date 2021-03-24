
#include <iostream>
#include <string>

using namespace std;

int main() {
  int first_class;
  int business_class;
  int economy_class;

  string destination_city, dep_city;

  // a = the crew and the pilot on board.

  int total_passengers;
  int a = 5;
  int b = 205;
  int c = 100;

  double percentage;

  cout << "How many first class passengers are boarding: ";
  cin >> first_class;

  cout << "How many business class passengers are boarding: ";
  cin >> business_class;

  cout << "How many economy class passengers are boarding: ";
  cin >> economy_class;

 
  std::cout << "Enter departure_city: "<<endl; //error is here cin is not working.
  std::getline(std::cin, dep_city); // not taking input

  cout << "Enter destination city: ";
  getline(cin, destination_city);
  std::cout << destination_city << std::endl;

  total_passengers = first_class + business_class + economy_class;

  percentage = (total_passengers / b) * c;

  cout << "The flight from " << dep_city << " to " << destination_city
       << " will have " << total_passengers << " passengers "
       << " (" << a + total_passengers << " souls on board)"
       << " and will be" << percentage << "full" << endl;

  return 0;
}
