/**
 * Created by ayoung on 16/09/17.
 */
import * as _ from "lodash";
import {Pipe, PipeTransform} from "@angular/core";

@Pipe({
    name: "personFilter"
})
export class PersonFilterPipe implements PipeTransform {

    transform(array: any[], query: string): any {
        if (query) {
            return _.filter(array, row=>row.name.indexOf(query) > -1);
        }
        return array;
    }
}
