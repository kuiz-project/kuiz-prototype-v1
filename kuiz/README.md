# 문제해결

## 문구가 변할때마다 애니메이션 주기

목표는 다음과 같다.
<img src="https://im.ezgif.com/tmp/ezgif-1-dfba0421ae.gif">

문구는 연습문제 => 해설 => 퀴즈 => "" => KUIZ순서대로 변하며 나타나고 사라질때 부드러운 애니메이션을 사용하는 것이다.

```js
function Home() {
  const [titlecount, setTitlecount] = useState(0);
  const [isfading, setIsFading] = useState(false);
  const point = ["연습문제", "해설", "퀴즈", "", "KUIZ"];
  useEffect(() => {
    const timer = setTimeout(() => {
      if (titlecount >= 4) {
        clearTimeout(timer); // KUIZ일때 타이머 멈추기
      } else {
        setIsFading(true); // 숨기기
        setTimeout(() => {
          // 1초 뒤
          setTitlecount((prev) => prev + 1); // 다음 문구 설정
          setIsFading(false); // 보이기(동시에 일어남)
        }, 1000);
      }
    }, 2000);
    return () => clearTimeout(timer);
  }, [titlecount]);

  return (
    <Wrapper>
      <Logo></Logo>
      <Title titlecount={titlecount} isfading={isfading}>
        당신이 원하는 <span>{point[titlecount]}</span>
      </Title>
      <StartButton>
        <span>시작하기</span>
      </StartButton>
    </Wrapper>
  );
}
```

```js
export const Title = styled.div`
  margin: 264px 605px 431px 80px;
  font-weight: 400;
  font-size: 128px;
  line-height: 185px;
  color: #515151d6;
  span {
    transition: opacity 1s ease-in-out;
    opacity: ${(props) => (props.isfading ? "0" : "1")};
    color: ${(props) => (props.titlecount >= 4 ? "#28527A" : "#515151d6")};
  }
`;
```

먼저, 이 `useEffect` 훅은 `titlecount`의 상태가 변경될 때마다 실행된다.

`useEffect` 내부에서 `setTimeout` 함수가 두 번 사용되고 있다.

첫 번째 `setTimeout`은 2초 후에 실행되며, 이 때 `setIsFading(true);`가 호출되어 `isFading` 상태를 `true로` 변경합니다. 이는 화면에 표시되는 텍스트가 사라지는 것을 의미한다. 이 `setIsFading(true)`;가 호출되면, `Title` 컴포넌트의 `isFading` 속성이 `true`로 변경되어 `opacity`가 0이 되고, 텍스트는 부드럽게 사라진다.

그 다음으로, 첫 번째 `setTimeout` 내부에서 또 다른 `setTimeout` 함수가 있는데 이 함수는 첫 번째 `setTimeout` 함수가 호출된 후 1초후에 실행된다.

여기서는 다음문구로 전환, 문구를 보이게 하는 함수를 실행한다.

따라서, 다음 문구는 부드럽게 나타난다.

여기서 주의 할 점은 setTimeout안의 두 호출 사이에 렌더링이 일어나지 않는다.

리액트는 내부적으로 성능최적화를 위해 업데이트를 한 번에 처리하여 한 번만 렌더링이 발생시킨다.

마지막으로, `clearTimeout`를 사용하고 있다. 이는 컴포넌트가 언마운트되거나 `titlecount` 상태가 변경되기 전에 현재 실행되고 있는 `setTimeout` 함수를 취소하는 역할을 한다. 이렇게 하지 않으면, 컴포넌트가 언마운트된 후에도 setTimeout 함수가 실행되는 문제를 방지할 수 있다.

**순서 정리**

최초 문구 보이기 => 2초뒤 가리기 => 1초뒤 문구 업데이트 + 보이기 => 1초 뒤에 다시 가리기 => ... `titlecount`가 4가될때 까지 반복 후

결국 2초동안 1초는 함수를 실행하는 시간 + 1초는 애니메이션 시간으로 인해 끊기지 않고 문구가 사라졌다 보였다 반복한다.

매우 자주 쓰이는 애니메이션인데도 라이브러리 없이 구현하는것이 마냥 쉽지만은 않다..

타이머안에 타이머를 넣는 것도 앞으로 고려해보자.
