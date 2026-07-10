import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class EmployeeEntity {
    @Id
    private Long id;
    private String name;

    public EmployeeEntity() {}
}
