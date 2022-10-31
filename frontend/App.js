import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

const Person = (props) => {
  return (
    <View>
      {
        props.age ?
          <Text style={styles.text}> Je Suis: {props.name} | age: {props.age}</Text>  : 
          <Text style={styles.text}> Je Suis: {props.name} </Text>

      }
    </View>
  )
}

export default function App() {


  return (
    <View style={styles.container}> 
      <Person name='yves'></Person>
      <Person name='Jeam'></Person>
      <Person name='Petit yvelos' age='14'></Person>
    </View>
  );
}


const styles = StyleSheet.create(
  {
    container: {
    marginTop: 60, 
    flexDirection: 'column',
    },
    text: {
      fontSize: 20
    }
  }
)