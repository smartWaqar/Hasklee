import System.Environment
import Debug.Trace

factorial 0 0 = 1
factorial 1 1 = 1 
factorial n a = n

--main = print (factorial 5)

main = do
       --putStrLn "enter value for x: "
       --input1 <- getLine
       minput1 <- getArgs
       let input1 = head minput1
       let instrxx3567 = (read input1 :: Int)
       print (factorial instrxx3567 2)