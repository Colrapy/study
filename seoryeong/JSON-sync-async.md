# 브라우저와 서버와의 통신
## HTTP(Hypertext transfer protocol)
**HTTP는 Client와 Server가 통신하는 방법에 대해 정의한**, 어떻게 Hypertext를 서로 주고받을 수 있는지를 규약한 **프로토콜**이다. 

Client가 Server에게 데이터를 요청할 수 있고, Server는 Client가 요청한 것에 따라서 그에 맞는 응답을 보내준다. 

> Hypertext?
: Hypertext란 웹 사이트에서 이용되는 하이퍼링크, 리소스들, 문서, 이미지 등을 의미한다.

## AJAX(Asynchronous Javascript and XML)
웹페이지에서 **동적으로** Server에게 데이터를 요청해서 받아올 수 있는 방법이다. 

## XHR(XMLHttpRequest)
이 Object는 브라우저 API에서 제공하는 Object 중 하나로, 이를 이용하면 **서버에게 간단한 방법으로 데이터를 요청하고 받을 수 있다. **
특히 `fetch() API`를 이용하면 간편하게 데이터를 주고받을 수 있지만, 이는 Internet Explorer에서는 지원되지 않기 때문에 잘 알아보고 사용해야 한다.

## XML
HTML과 같은 **마크업 언어 중 하나**로, **데이터를 표현할 수 있는 또다른 방법**이다. 
그러나 XML을 이용하면 불필요한 태그들이 너무 많이 들어가서 파일의 용량도 커지고, 가독성도 좋지 않아 많이 사용하지 않는 추세이다. 

# 서버와 데이터 교환 시 이용하는 또다른 방법: JSON 
## JSON(JavaScript Object Noation)
JSON은 JavaScript 객체 리터럴이나 배열 리터럴의 문법과 매우 유사하다. 

브라우저 뿐만아니라 모바일에서 서버와 데이터를 주고받을 때, 서버와 통신하지 않아도 Object를 파일 시스템에 저장할 때에도 사용한다.

1. 데이터를 주고받을 때 쓸 수 있는 가장 간단한 파일 포맷
2. 텍스트를 기반으로 제작되어 용량이 작고, 읽기 편한 파일 포맷
3. Key와 Value의 쌍으로 이루어져 있음
4. 데이터를 서버와 주고받을 때 ***직렬화***하기 위해, 전송할 때 씀
5. **프로그램 언어나 플랫폼에 상관없이 쓸 수 있음**

> 객체 직렬화(serialize)
: 객체 직렬화란 **객체의 상태**를 **문자열로 변환하는 과정**을 의미한다. 
아래에서 자세히 알아보자. 

## 객체 직렬화하기
객체의 상태를 문자열로 변환하는 과정을 **객체 직렬화**라고 한다. 이때 생성된 문자열은 나중에 객체 복원에 사용할 수 있다. **ES5는 `JSON` Object를 이용하여 JavaScript 객체를 직렬하고, 객체를 복원하는 메서드를 지원한다.**

### JSON에서 지원하는 2가지 메서드
- **객체를 직렬화**하는 메서드 **`JSON.stringify()`**
  - 객체가 가진 **열거 가능한 고유 프로퍼티만 직렬화 한다.**
  - 만약 어떤 프로퍼티 값을 직렬화할 수 없다면, 해당 프로퍼티 값은 직렬화 결과에 포함되지 않는다. 
- **문자열을 객체로 복원**하는 메서드 **`JSON.parse()`**

`JSON.stringify()`와 `JSON.parse()`는 두 번째 선택 인자를 갖는다. 이 인자를 사용해 직렬화 또는 복원할 프로퍼티 목록을 지정할 수 있다. 

### JSON 문법은 JavaScript 문법의 부분 집합 
JSON 문법은 JavaScript 문법의 부분 집합이기에 JavaScript의 모든 값을 표현할 수는 없다. 

- **직렬화와 복원이 가능한 값들**
  - 객체
  - 배열
  - 문자열
  - 유한한 수
  - boolean (true, false)
  - null

- **직렬화는 되는데 복원이 안되는 값들?**
  - NaN(Not a Number), Infinity, -Infinity는 `null`로 직렬화 된다.
  - Date 객체는 문자열로 직렬화 된다.
  
- **직렬화와 복원이 아예 안되는 값들**
  - Function
  - RegExp
  - Error
  - undefined

>  Date객체
: `Date.toJSON()`으로 Date 객체를 문자열로 직렬화할 수 있지만, `JSON.parse()`함수는 문자열을 Date 객체로 복원할 수 없다. 


# JSON object 이용해보기
## 1. object를 JSON으로 변환하기 - `JSON.stringfy(obj)`

```js
// 1. 불리언타입
let jsonBool = JSON.stringify(true);
console.log(jsonBool); // true

// 2. 배열타입
jsonArr = JSON.stringify(['apple', 'banana']);
console.log(jsonArr); // ["apple", "banana"]

// 3.객체 타입
// 단, 함수나 JavaScript만의 Symbol은 JSON으로 변환되지 않는다. 
const cat = {
	name: 'kitty',
  	color: 'white',
  	size: null,
  	birthDate: new Date(),
  	symbol: Symbol("id"),
  	grooming: function() { 
    	console.log(`${this.name} is grooming!`);
    },  
}

jsonObj = JSON.stringify(cat);
console.log(jsonObj); // {"name":"kitty","color":"white","size":null,"birthDate":"2022-01-10T13:53:24.756Z"}

jsonChoose = JSON.stringify(cat, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'cutiy' : value;  
});
/* key: , value: [object Object]
key: name, value: kitty
key: color, value: white
key: size, value: null
key: birthDate, value: 2022-01-10T13:53:24.756Z */

console.log(jsonChoose);
```

## 2. JSON을 Object로 바꾸기 - `JSON.parse(json)`

```js
const cat = {
	name: 'kitty',
  	color: 'white',
  	size: null,
  	birthDate: new Date(),
  	symbol: Symbol("id"),
  	grooming: function() { 
    	console.log(`${this.name} is grooming!`);
    },  
}

json = JSON.stringify(cat);
console.log(json); // {"name":"kitty","color":"white","size":null,"birthDate":"2022-01-10T14:13:45.244Z"}

const obj = JSON.parse(json, (key, value) => {
 	console.log(`key: ${key}, value: ${value}`);
  	return key === 'birthDate' ? new Date(value) : value;
});
/* key: name, value: kitty
key: color, value: white
key: size, value: null
key: birthDate, value: 2022-01-10T14:15:55.973Z
key: , value: [object Object] */

console.log(obj); // {name: 'kitty', color: 'white', size: null, birthDate: Mon Jan 10 2022 23:15:55 GMT+0900 (한국 표준시)}

cat.grooming(); // kitty is grooming!

console.log(cat.birthDate.getDate()); // 10
console.log(obj.birthDate.getDate());

```

---
# Callback 함수

JavaScript는 동기적인 언어이다. 호이스팅이 된 이후부터 코드가 작성한 순서에 따라 하나씩 동기적으로 실행되기 때문이다. 

> hoisting?
: 호이스팅이란 var 변수의 선언이나 함수 선언들이 가장 위로 올라가는 것을 의미한다.

# JavaScript의 비동기?

그렇다면 JavaScript에서 말하는 **'비동기'** 란 무엇일까? 비동기는 언제 코드가 실행될 지 예측할 수 없는 것이다. 비동기의 좋은 예는 `setTimeout()`이 있다. 이는 지정한 시간이 지나면 전달한 콜백함수를 호출한다. 

> callback 함수
: 콜백함수는 파라미터로 전달한 함수를 나중에 불러달라고 하는 것과 같다.

## 콜백함수 알아보기

setTimeout은 바로 실행되는 것이 아니라, 인자로 함수를 전달하고 있다. 그래서 지금 당장 실행하지는 않고, 정해진 시간이 지난 후에 파라미터로 전달한 함수를 실행한다. 보통 콜백함수는 arrow함수로 나타낸다. 

```js
console.log('1');
// setTimeout(function() { console.log('2');}, 1000); 
setTimeout(() => console.log('2'), 1000); // 1초 뒤에 2가 출력된다.
console.log('3');

// 결과
// 1
// 3
// 2
```

그렇다면 콜백은 항상 비동기일때에만 쓰는 것일까?

# callback의 2가지 경우
## 1. synchronous callback
즉각적으로, 동기적으로 실행하는 콜백이다. 콜백을 파라미터 인자로 받아서, 이를 처리하는 함수를 만들어보자.

```js
function printImmediately(write) { // 함수의 선언
	write();
}

printImmediately(() => console.log('hello'));
```

함수의 선언은 호이스팅이 되니 가장 위에서 실행되는 효과를 가진다.

## 2. asynchronous callback
나중에 언제 실행될 지 예측 불가능한 콜백이다. 

```js
function printWithDelay(print, timeout) { // setTimeout을 wrapping 하고 있는 함수 
 	setTimeout(print, timeout);  
}

printWithDelay(() => console.log('async callback'), 2000);
```

async callback은 2초뒤에 콘솔에 찍히게 된다.

# callback Hell, 콜백 지옥
콜백지옥이란 끊임없이 콜백을 부르고 또 부르고,, 이렇게 작성된 코드를 일컫는 말이다. 콜백 체인의 문제점은 무엇일까?

1. 가독성이 떨어지고, 한눈에 알아보기 어렵다.
2. 로직 파악이 어렵고 유지 보수가 없다.
3. 체인이 길어질수록 에러 발생확률이 높고 디버깅도 어려워진다.

직접 콜백 지옥에 빠져보다. 이번에는 백엔드로부터 데이터를 받아오는 클래스를 작성해보자.

```js
class UserStorage {  
  loginUser(id, password, onSuccess, onError) {
    setTimeout(() => {
      if (
        (id === 'muz' && password === 'velogs')
      ) {
        onSuccess(id);
      } else {
        onError(new Error('not found'));
      }
    }, 2000);
  }

  // 성공 시 사용자의 데이터를 받아서 사용자의 역할을 서버에게 요청해서 받아옴
  getRoles(user, onSuccess, onError) { 
    setTimeout(() => {
      if (user === 'muz') {
        onSuccess({ name: 'muz', role: 'admin' });
      } else {
        onError(new Error('no access'));
      }
    }, 1000);
  }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
  id,
  password,
  user => {
    userStorage.getRoles(
      user,
      userWithRole => {
        console.log(
          `Hello ${userWithRole.name}, you have a ${userWithRole.role} role`
        );
      },
      error => {
        console.log(error);
      }
    );
  },
  error => {
    console.log(error);
  }
);                               
```

---
# promise

# 비동기를 처리하는 방법 `Promise`
프로미스는 JavaScript안에 내장된 Object이다. 이는 비동기를 간편하게 처리할 수 있도록 도와주는 Object로, 콜백함수 대신 사용할 수 있다. 정해진 장시간의 기능을 수행한 후 정상적으로 기능이 수행되어진다면 성공의 메시지와 함께 처리된 데이터를 제공하고, 만약 기능을 수행하다가 예상치 못한 오류가 발생하면 에러를 전달한다. 

## Promise의 2가지 Point
### 1. state - 3가지 상태 구분하기
: promise가 만들어져서 지정한 오퍼레이션이 수행중일때에는 **Pending 상태**가 되고, 해당 오퍼레이션이 성공적으로 끝나면 바로 **fulfilled 상태**가 된다. 예기치 못한 오류(파일을 찾을 수 없거나 네트워크에 문제가 생긴다면)가 발생한다면 **rejected 상태**가 된다. 

때문에 프로세스가 무거운 연산(operation)을 수행하고 있는지, 연산이 모두 완료되어서 성공했는지 or 실패했는지에 대한 상태를 이해하는 것이 중요하다.

### 2. Producer와 Consumer의 차이점 이해하기
: 원하는 데이터를 제공하는 사람(Producer)와 이 제공된 데이터를 쓰는 사람(Consumer)의 차이점을 이해하는 것이 중요하다. 

# 자세히 알아보기
## producer ?
promise는 class여서 new 키워드를 사용해 원하는 Object를 생성할 수 있다. 
![](https://images.velog.io/images/muz/post/279ef204-4c9a-4954-9677-ad4e37a6cefd/image.png)
해당 사진을 보면 알 수 있듯이, Promise의 생성자에 **`executor`** 라는 콜백함수를 전달해주어야한다. 이 콜백함수는 또 다른 두가지의 콜백함수를 받는다.

1. **resolve**
: 기능을 정상적으로 수행해서 마지막에 최종 데이터를 전달하는 콜백함수

2. **reject**
: 기능을 수행하다가 중간에 문제가 생기면 호출하게 될 콜백함수

보통 Promise 내에서는 조금 해비한 일들을 한다. 주로 네트워크에서 데이터를 받아오거나, 파일에서 큰 데이터를 읽어오는 작업을 한다. 이러한 작업들은 시간이 꽤 걸리는 작업으로, 이를 동기적으로 처리하게 되면 해당 작업을 하는 동안 그 다음라인의 코드가 실행되지 않게 된다. 때문에 **시간이 다소 걸리는 작업들은 promise를 만들어서 비동기적으로 처리하는 것이 좋다.**

아래의 코드는 프로미스를 생성하고, executor로 resolve와 reject 콜백함수를 전달한다. 네트워크 통신을 하는 것처럼 보이기 위해 2초간 어떤 일을 하다가, 결과를 주는 코드로 작성했다. 
```js
const promise = new Promise((resolve, reject) => {
  console.log('doing something...');
  
  // 네트워크 통신을 하는 것처럼 setTimeout으로 딜레이 주기
  setTimeout(() => {
    resolve('muz');
    // reject(new Error('no network'));
  }, 2000);
});
```

> promise가 생성되어질 때에는 전달한 `executor` 콜백함수가 바로, 자동적으로 실행된다.

위의 코드를 보면, new 키워드로 promise를 생성하는 순간 **즉시실행함수로 인해 `executor` 콜백함수가 바로 실행**되는 것을 알 수 있다. promise안에 네트워크 통신을 하는 코드를 작성했다면, promise가 만들어지는 순간 바로 네트워크 통신을 수행하게 된다는 것이다.

만약 네트워크 요청이 사용자가 요구하는 경우에 일어나야 하는 것이라면(ex. 사용자가 버튼을 눌렀을 때 네트워크 통신이 일어나는 경우), 사용자가 요구하지 않았음에도 불필요한 네트워크 통신이 일어날 수 있다는 것이다. 

위의 코드에서 성공적으로 일이 마무리되면 resolve를 통해 데이터를 전달하고, 예기치 못한 에러가 발생하게되면 Error Object를 통해 에러 값을 전달한다. 이 Error Object는 JS에서 제공하는 Object중 하나이다.

## Consumer ?
위의 producer 부분에서 작성한 promise를 사용해보자. consumer는 **`then`, `catch`, `finally`** 를 통해 값을 받아올 수 있다. 

```js
promise
	.then(value => {
  		console.log(value);
    })
    .catch(error => {
      	console.log(error);
    })
    .finally(() => {
      	console.log('finally');
    });
```
1. **`then`**
- then은 promise가 정상적으로 잘 수행되어서 마지막에 최종적으로 resolve 콜백함수를 통해 전달한 값이 value의 파라미터로 전달되어 들어온다.
-  promise에 then을 호출하게되면, 이 then은 결국 똑같은 promise를 return한다.

2. **`catch`**
- 만약 promise에서 resolve 대신 reject를 호출하게 되면, 콘솔에서 에러를 만나게 된다.
- reject는, catch를 이용해 에러가 발생했을 때 이를 어떻게 처리할 지 콜백함수를 등록할 수 있다. 
- 위의 then에서 return한 promise에 catch를 다시 호출할 수 있다. (promise chaining)

3. **`finally`**
- then과 catch를 이용해서 성공한 값, 실패한 에러를 받아와서 원하는 방식으로 처리한 뒤, 
성공, 실패 여부에 상관없이 어떤 기능을 마지막에 수행하고 싶다면 `finally`를 사용할 수 있다.