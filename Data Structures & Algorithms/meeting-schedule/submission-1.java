/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
       
  
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
         for (Interval interval : intervals) {
            System.out.println("Start: " + interval.start + ", End: " + interval.end);
        }
        Collections.sort(intervals, Comparator.comparingInt(i -> i.start));
       for (Interval interval : intervals) {
            System.out.println("Start: " + interval.start + ", End: " + interval.end);
        }
        for(int i = 1; i < intervals.size(); i++){
            Interval i1 = intervals.get(i-1);
            Interval i2 = intervals.get(i);

            if(i1.end > i2.start){
                return false;
            }
        }
        return true;

    }
}
